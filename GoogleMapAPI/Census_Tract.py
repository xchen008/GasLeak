from urllib.request import urlopen                       # Getting the json data from the url
import requests
import json
import pandas as pd                                     # To read and write csv files
import time

csvfile = "FDNY2018.csv"


### GETTING CENSUS DATA FROM COORDS AND ADDING TO CSV ####

# FUNCTION: Get Census Tract from Longitude and Latitude coordintes using the Census Beru's API which returns a JSON file
def getCensusTract(longitude, latitude, retryRun=0):  # returns an array [CensusTrack, CensusBlock, CountyName]
    url = "https://geocoding.geo.census.gov/geocoder/geographies/coordinates?y={0}&x={1}&benchmark=Public_AR_Current&vintage=Current_Current&format=json".format(
        longitude, latitude)
    if retryRun == 11:  # Failed to get json data 11 times with this longitude and latitude so need to skip this one
        print("failed 11 times")
        return [str(0), str(0), str(0)]
    try:
        response = requests.get(url)
        dataJSON = response.json()
        data = dataJSON["result"]
        track = data["geographies"]["Census Tracts"][0]["BASENAME"]
        block = data["geographies"]["2010 Census Blocks"][0]["BLOCK"]
        county = data["geographies"]["Counties"][0]["NAME"]
        return [str(track), str(block), str(county)]
    except:
        retryRun += 1
        print("******** Error on longitude, latitude: " + str(longitude) + "," + str(
            latitude) + " ------ retrying " + str(retryRun))
        return getCensusTract(longitude, latitude, retryRun)  # *****need to return the recursive function


# a) Will modify GasHistory_ConEdison.csv to have the CensusTract, CensusBlock, and CountyName columns

df = pd.read_csv(csvfile)  # read the csv file and store to df

for row in range(21000, len(df)):
    # b) using the lat and long coords of each entry to find the census data and adding to the respective arrays to add to csv col later
    returnArray = getCensusTract(float(df.loc[row]["lat"].item()),
                                 float(df.loc[row]["lon"].item()))  # data.iat[i,4] = lat   # data.iat[i,5] = lon
    df.iat[row, 6] = returnArray[0]
    df.iat[row, 7] = returnArray[1]
    df.iat[row, 8] = returnArray[2]

df.to_csv("FDNY_21000.csv", encoding='utf-8',index=False)