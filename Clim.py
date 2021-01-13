import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Clim_data = pd.read_csv("Clim.csv")
#Extract years and rainfall
years = np.array(Clim_data["Year"])
rain = np.array(Clim_data["Total Rainfall (mm)"])

#Set up figure and subplot
fig = plt.figure()
ax_rain = fig.add_subplot(1,1,1)

#plot the bar chart, normal rainfall betweem 2150 and 2650 mm/year
high_index = rain > 2650
high_bar = ax_rain.bar(years[high_index], rain[high_index], color="aqua", label="Higher than normal")
normal_bar = ax_rain.bar(years[np.logical_and(rain > 2150, rain < 2650)], rain[np.logical_and(rain > 2150, rain < 2650)], color="green", label="Normal")
low_bar = ax_rain.bar(years[rain < 2150], rain[rain < 2150], color="peru", label="Lower than normal")

#add legend, title, labels, set the limit of y-axis
ax_rain.legend()
ax_rain.set_xlabel("Year")
ax_rain.set_ylabel("Rainfall (mm)")
ax_rain.set_title("Yearly Precipitation at HKO")
ax_rain.set_ylim(0,4000)
ax_rain.set_xticks(np.arange(1960,2020,5))

fig.savefig("Clim.png",dpi=300)


