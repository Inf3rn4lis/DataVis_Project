import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Creates A scatter plot graph for the average temp.
Includes trend line!
'''


'''
Graphing Mullingar Average
'''
yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (12,8))
avgScatter = ax.plot(yearlyWeather["Year"], yearlyWeather["Avg_Mean_Temp"], color = "tab:green", alpha = 0.3)

# calculate equation for trendline
z_avg = np.polyfit (yearlyWeather["Year"],yearlyWeather["Avg_Mean_Temp"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(yearlyWeather["Year"], trendlineEq(yearlyWeather["Year"]), label = "Mullingar Average", alpha = 1, color = "tab:green")




'''
Graphing Global
'''
globalWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/NASAGlobalAvgTemp.csv")

# Plot the average temperture


avgScatter = ax.plot(globalWeather["Year"], globalWeather["Avg-Temp"], color = "tab:cyan", alpha = 0.3)

# calculate equation for trendline
z_avg = np.polyfit (globalWeather["Year"],globalWeather["Avg-Temp"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(globalWeather["Year"], trendlineEq(globalWeather["Year"]), label = "Global Average", alpha = 1, color = "tab:cyan")

# Legend
ax.legend(title = "Temp Type")
#Lables
ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Mullingar Vs Global Average Temperture Graph")

plt.show()
