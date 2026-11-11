import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Creates A scatter plot graph for the average temp.
Includes trend line!
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (16,8))
avgScatter = ax.scatter(yearlyWeather["Year"], yearlyWeather["Avg_Mean_Temp"], marker = "o", label = "Average")

# calculate equation for trendline
z_avg = np.polyfit (yearlyWeather["Year"],yearlyWeather["Avg_Mean_Temp"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(yearlyWeather["Year"], trendlineEq(yearlyWeather["Year"]), label = "Average Trendline", color = "darkblue")


ax.legend(title = "Temp Type")

#Lables
ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Yearly Average Temperture Graph")

plt.show()
