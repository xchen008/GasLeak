import os
import pandas as pd
import geopandas as gpd
import platform
import matplotlib.pyplot as plt

us_tract = gpd.read_file('tl_2019_36_tract/tl_2019_36_tract.shp')
us_tract.plot()
plt.show()