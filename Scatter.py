import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress as reg #needed for linear regression

Jan_data = pd.read_csv("Jan2017.csv")

# Extracting pressure and temperature
temp = Jan_data["Mean (deg. C)"][0:31]
pressure = Jan_data["Mean Pressure (hPa)"][0:31]

# Set up figure and subplot
fig = plt.figure()
ax_tp = fig.add_subplot(1,1,1)

# draw the scatter plot
dot = ax_tp.scatter(pressure, temp, label="raw data")

# linear fit, try printing out fit to see what are included
fit = reg(pressure, temp)
slope = fit[0]
intercept = fit[1]

# regression line, equation: y(temp) = slope * x(pressure) + intercept
line = ax_tp.plot(pressure, slope*pressure + intercept, color="red", label="linear fit")
equation = "T = " + str(round(slope,2)) + "*P + " + str(round(intercept,2))
ax_tp.text(1022, 19, equation)

# add legend, title, labels.
ax_tp.legend()
ax_tp.set_xlabel("Pressure (hPa)")
ax_tp.set_ylabel("Temperature (deg C)")
ax_tp.set_title("Temperature vs Pressure in Jan 2017 at HKO")

fig.savefig("Scatter.png",dpi=300)




