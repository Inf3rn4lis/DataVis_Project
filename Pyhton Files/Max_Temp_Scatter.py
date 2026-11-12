
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Creates A scatter plot graph for the maximum temp.
Includes trend line!
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (16,8))
avgScatter = ax.scatter(yearlyWeather["Year"], yearlyWeather["Max_Temp"], marker = "o", label = "Maximum", color = "tab:orange")

# calculate equation for trendline
z_avg = np.polyfit (yearlyWeather["Year"],yearlyWeather["Max_Temp"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(yearlyWeather["Year"], trendlineEq(yearlyWeather["Year"]), label = "Maximum Trendline", alpha = 0.5, color = "tab:orange")


ax.legend(title = "Temp Type")

#Lables
ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Mullingar Yearly Maximum Temperture Graph")

plt.show()
