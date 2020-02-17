import os
import pandas as pd

data2018 = pd.read_csv('FDNY2018.csv')
data2017 = pd.read_csv('FDNY_2017.csv')

data2017['lat'] = 0.0
data2017['lon'] = 0.0
data2017['CountyName'] = '0'
data2017['Geoid2010'] = 0

for row in range(0,len(data2017)):
    