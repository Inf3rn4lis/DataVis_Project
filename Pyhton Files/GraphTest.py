import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Creates A graph that displays the Average, Minimum and Maximum yearly temperture.

While visualy interesting, this stretches the graph thin and makes any trend hard to see.
'''

yearlyWeather = pd.read_csv("https://raw.githubusercontent.com/Inf3rn4lis/DataVis_Project/main/Databases/Modified/YearlyDataOnly.csv")



fig, ax = plt.subplots(figsize = (16,12))

#Average temp
avgLine = ax.plot(yearlyWeather["Year"], yearlyWeather["Avg_Mean_Temp"], linewidth = 2, label = "Average", color = "tab:green")


# Max Temp
maxLine = line = ax.plot(yearlyWeather["Year"], yearlyWeather["Max_Temp"], linewidth = 2, label = "Max", color = "tab:orange")

# Min Temp
minLine = ax.plot(yearlyWeather["Year"], yearlyWeather["Min_Temp"], linewidth = 2, label = "Min", color = "tab:blue")

ax.legend(title = "Temp Type")

ax.set_xlabel('Year')
ax.set_ylabel('Temperture (*C)')

ax.set_title("Mullingar Yearly Tempertures Graph")

plt.show()