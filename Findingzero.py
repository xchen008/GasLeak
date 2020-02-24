import numpy as np
import pandas as pd

#data2017 = pd.read_csv('FDNY_2017.csv')
#unproc = pd.DataFrame(columns=['incident_datetime', 'alarm_box_borough', 'zipcode','alarm_box_location','lat','lon','CountyName','Geoid2010'])
#ind = 0
#for row in range(0,len(data2017)):
#    if data2017.at[row,'Geoid2010'] == 0 and data2017.at[row,'alarm_box_location'] not in unproc.alarm_box_location.values:
#        unproc.loc[ind] = data2017.loc[row]
#        ind += 1

#unproc.to_csv('unproc.csv', encoding='utf-8',index=False)

df = pd.read_csv("FDNY2018.csv")
data  = df[['incident_datetime','alarm_box_borough','zipcode','alarm_box_location','lat','lon','CountyName','Geoid2010']].copy()

data.to_csv('FDNY2017_18.csv', encoding='utf-8',index=False)
