import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Creates A graph that displays the Average, Minimum and Maximum yearly temperture.

While visualy interesting, this stretches the graph thin and makes any trend hard to see.
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (16,8))
avgLine = ax.plot(yearlyWeather["Year"], yearlyWeather["Avg_Mean_Temp"], marker = "o", linewidth = 2, label = "Average")
maxLine = line = ax.plot(yearlyWeather["Year"], yearlyWeather["Max_Temp"], marker = "o", linewidth = 2, label = "Max")
minLine = ax.plot(yearlyWeather["Year"], yearlyWeather["Min_Temp"], marker = "o", linewidth = 2, label = "Min")

ax.legend(title = "Temp Type")

ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Yearly Average Temperture Graph")

plt.show()