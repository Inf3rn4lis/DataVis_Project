import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

print('Rows:', len(yearlyWeather))
print(yearlyWeather.to_string())

'''
fig, ax = plt.subplots(figsize = (8,4))
ax.plot(yearlyWeather[""]


ax.set_title("Yearly Temperture Graph")
'''