#%%

import os
import pandas as pd
import geopandas as gpd
import platform
import matplotlib.pyplot as plt
import contextily as ctx

#shp_file = 'tl_2019_36_tract/tl_2019_36_tract.shp'
shp_file = 'nyu_2451_34505/nyu_2451_34505.shp'
#shp_file = 'NYC_Census_Tracts_for_2010_US_Census/NYC_Census_Tracts_for_2010_US_Census.shp'
csvfile = 'Geoid_Count2018.csv'
us_tract = gpd.read_file(shp_file)
data = pd.read_csv(csvfile)

#%%
Month_data = pd.DataFrame(columns = ['Time','Geoid','NumberOfReports']) # create a new Dataframe with each month
for row in range(0,len(data)):
    if data.iat[row,0][0:2] == '01':    
        Month_data = Month_data.append({'Time' : data.iat[row,0], 'Geoid' : data.iat[row,1],  'NumberOfReports': data.iat[row,2] } , ignore_index=True)

#%%
us_tract['Geoid'] = us_tract['tractid'].str.upper()              # create a new column of the same name as DF from 'NAME'
                                                                    # In shp file, the "NAME" is the census tract
                                                                    # In shp file, the "tractid" is the geoid
us_tract['Geoid'] = us_tract.Geoid.astype(float)        # Conver type to float so we can merge the DFs
                                                                 # We use merge to pass in the data(NumOfReports)from the csv
Month_data['Geoid'] = Month_data.Geoid.astype(float)
Month_data['NumberOfReports'] = Month_data.NumberOfReports.astype(int)
join = us_tract.merge(Month_data, on='Geoid')

#%%
# Merging in another way
#us_tract['NumberOfReports'] = 0
#for row in range(0,len(us_tract)):
#    
#    ind = Month_data.loc[Month_data['Geoid'] == us_tract['Geoid'][row]].index
#    if len(ind) is not 0:
#        us_tract.at[row,'NumberOfReports'] = Month_data['NumberOfReports'][ind[0]]


#%%
#map = us_tract.plot(column='NumberOfReports',cmap='Greens',figsize = (10,8),alpha = 0.8,legend = True)#edgecolor = 'k'
#leg = map.get_legend()
#leg.set_title('Number Of Gas Leak Reports')
#leg.set_bbox_to_anchor((1.1,0.5,0.1,0.5))                          # Adjusted numbers to find the best location and size of the legend
#%%
#plot with background map
Total = join['NumberOfReports'].sum()
df = join.to_crs(epsg=3857) 
ax = df.plot(column='NumberOfReports',cmap='Greens',figsize = (10,8),alpha = 0.8,legend = True)
ax.set_title(label = 'Number of Gas Leak Reports per Census Tract (' + 'January' + ')' + '( Total number of reports: '+ str(Total)+')', fontdict={'fontsize': 16}, loc='center')
ctx.add_basemap(ax,zoom = 12)





# %%
#print(us_tract['COUNTYFP'])

#nyc_county = ['005','047','061','081','085']
#nyc_tract = us_tract[(us_tract['COUNTYFP'] == nyc_county[0]) | (us_tract['COUNTYFP'] == nyc_county[1]) | (us_tract['COUNTYFP'] == nyc_county[2]) | (us_tract['COUNTYFP'] == nyc_county[3]) |( us_tract['COUNTYFP'] == nyc_county[4])]

count = 0
for row in range(0,len(Month_data)):
    ind = Month_data.loc[Month_data['Geoid'] == us_tract['Geoid'][row]].index
    if len(ind) is 0:
        #print(us_tract['Geoid'][row])
        count += 1

print(count)
print(len(us_tract))


# %%
print(list(join))
print(join.bcode)
# %%
