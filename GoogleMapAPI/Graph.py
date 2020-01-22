#%%

import os
import pandas as pd
import geopandas as gpd
import platform
import matplotlib.pyplot as plt

us_tract = gpd.read_file('tl_2019_36_tract/tl_2019_36_tract.shp')
#us_tract.plot()
#plt.show()
#print(list(us_tract))
data = pd.read_csv('CT_Monthly_Count2018.csv')
Month_data = pd.DataFrame(columns = ['Time','CensusTract','NumberOfReports']) # create a new Dataframe with each month
for row in range(0,len(data)):
    if data.iat[row,0][0:2] == '12':    
        Month_data = Month_data.append({'Time' : data.iat[row,0], 'CensusTract' : data.iat[row,1],  'NumberOfReports': data.iat[row,2] } , ignore_index=True)

#%%
ok_tract = us_tract[us_tract['STATEFP'] == '36']                        # select all data
ok_tract['CensusTract'] = ok_tract['NAME'].str.upper()              # create a new column of the same name as DF from 'NAME'
                                                                    # In shp file, the "NAME" is the census tract
ok_tract['CensusTract'] = ok_tract.CensusTract.astype(float)        # Conver type to float so we can merge the DFs
                                                                 # We use merge to pass in the data(NumOfReports)from the csv
join = ok_tract.merge(Month_data, on='CensusTract')
#%%
map = join.plot(column='NumberOfReports',cmap='Greens',figsize = (10,8),legend = True)
map.set_title(label = 'Number of Reports per Census Tract (December)', fontdict={'fontsize': 16}, loc='center')
leg = map.get_legend()
leg.set_title('Number Of Reports')
leg.set_bbox_to_anchor((1.1,0.5,0.1,0.5))                          # Adjusted numbers to find the best location and size of the legend
# %%
