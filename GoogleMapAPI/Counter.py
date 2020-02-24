import pandas as pd
import numpy as np

infile = "FDNY2017_18.csv"
outfile = "Geoid_Count2017_18.csv"

data = pd.read_csv(infile)

#info = np.array(['12/2018CT437.01','12/2018CT890.0']) # creating an numpy array of string
#info = np.array(['12/31/2018T15CT437.01','12/31/2018T15CT890.0']) 
info = np.array(['12/2018CT36047089000','12/2018CT36081043701']) 
count = np.array([0,0])                                           # keep track of the count in another array 

for row in range(0,len(data)):
    # creating a string with all the details we need
    detail = data.iat[row,0][5:7] + '/' + data.iat[row,0][0:4] + 'CT' + str(data.at[row,'Geoid2010'])
    #detail = data.iat[row,0][5:7] + '/' + data.iat[row,0][8:10] + '/' + data.iat[row,0][0:4] + 'T' + data.iat[row,0][11:13] + 'CT' + str(data.iat[row,6])
    
    if detail in info:                          # if the string already exist, we will just increment the count
        itemindex = np.where(info == detail)
        count[itemindex[0][0]] += 1
    else:                                       # else we will have to add the string to info array and create an extra count
        info = np.append(info,detail)
        count = np.append(count,1)


# write to dataframe and then csv file

#out = pd.DataFrame(columns = ['Date', 'Hour','CensusTract','NumberOfReports']) 
#for row in range(0,len(info)):
#    out = out.append({'Date' : info[row][0:10], 'Hour' : info[row][11:13], 'CensusTract' : info[row][15:],  'NumberOfReports': count[row] } , ignore_index=True)

out = pd.DataFrame(columns = ['Time','Geoid','NumberOfReports']) 
for row in range(0,len(info)):
    out = out.append({'Time' : info[row][0:7], 'Geoid' : info[row][9:],  'NumberOfReports': count[row] } , ignore_index=True)
out.to_csv(outfile, encoding='utf-8',index=False)