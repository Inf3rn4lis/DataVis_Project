import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

print('Rows:', len(yearlyWeather))

# average Mean temp over the entire year
#catagoryMeanTemp = (orders.groupby('category', as_index=False).agg(revenue=('revenue', 'sum'), order_count=('order_id', 'count')).sort_values('revenue', ascending=False))

# Highest temp in the year
#catagoryMaxTemp =

# Lowest temp in the year
#catagoryMinTemp = 

# Average wind speed over the year
#catagoryWindSpeed =

# precipitation amount in mm
#dcatagoryRain =
