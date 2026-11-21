
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Creates A scatter plot graph for the rainfall,
Includes trend line!
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")

# Plot the average temperture

fig, ax = plt.subplots(figsize = (16,8))
avgScatter = ax.scatter(yearlyWeather["Year"], yearlyWeather["Avg_mm_Rain"], marker = "o", label = "Average Monthly Rainfall", color = "tab:blue")

# calculate equation for trendline
z_avg = np.polyfit (yearlyWeather["Year"],yearlyWeather["Avg_mm_Rain"],1)
trendlineEq = np.poly1d(z_avg)

# apply trend line
ax.plot(yearlyWeather["Year"], trendlineEq(yearlyWeather["Year"]), label = "Rainfall Trendline", alpha = 0.5, color = "tab:blue")

# Correlation Coeffecient.
correlation_cof = np.corrcoef(yearlyWeather["Year"],yearlyWeather["Avg_mm_Rain"])[0,1]
print(correlation_cof)

corrcorrelation_cof = round(correlation_cof, 2)


#Lables
ax.set_xlabel('Year')
ax.set_ylabel('Average monthly mm of rain')

ax.set_title("Mullingar Average Monthly mm of Rain Per Year Graph\n R="+str(corrcorrelation_cof))

plt.show()
