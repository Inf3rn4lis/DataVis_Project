
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Creates A scatter plot graph for the min temp.
Includes trend line!
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (16,8))
avgScatter = ax.scatter(yearlyWeather["Year"], yearlyWeather["Min_Temp"], marker = "o", label = "Minimum", color = "tab:blue")

# calculate equation for trendline
z_avg = np.polyfit (yearlyWeather["Year"],yearlyWeather["Min_Temp"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(yearlyWeather["Year"], trendlineEq(yearlyWeather["Year"]), label = "Minimum Trendline", alpha = 0.5, color = "tab:blue")


ax.legend(title = "Temp Type")

#Lables
ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Mullingar Yearly Minimum Temperture Graph")

plt.show()
