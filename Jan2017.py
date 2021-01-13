import matplotlib.pyplot as plt
import matplotlib.dates as mdates #used to format date on x-axis
import pandas as pd
import datetime as dt

Jan_data = pd.read_csv("Jan2017.csv")

# Extracting pressure and temperature
mean_temp = Jan_data["Mean (deg. C)"][0:31]
min_temp = Jan_data["Absolute Daily Min (deg. C)"][0:31]
max_temp = Jan_data["Absolute Daily Max (deg. C)"][0:31]
pressure = Jan_data["Mean Pressure (hPa)"][0:31]
dates = Jan_data["Day"][0:31]

#Dates from 2017-01-01 to 2017-01-31
start = dt.datetime(year=2017, month=1, day=1)
end   = dt.datetime(year=2017, month=1, day=31)
dates = [start + dt.timedelta(days=x) for x in range(0, (end-start).days+1)]
#dates = pd.date_range(start=pd.datetime(2017,1,1), end=pd.datetime(2017,1,31), freq="1D")
for date in dates:
    print(date.strftime("%Y-%m-%d %H:%M:%S"))

#Figure and subplots
fig = plt.figure()
ax_temp = fig.add_subplot(2,1,1)
ax_pres = fig.add_subplot(2,1,2,sharex=ax_temp) #share the same x_axis with ax_temp

# Plot lines
max_line = ax_temp.plot(dates, max_temp, linestyle="-", color="r", label="Max Temp.")
mean_line = ax_temp.plot(dates, mean_temp, linestyle="-", color="lime", label="Mean Temp.")
min_line = ax_temp.plot(dates, min_temp, linestyle="-", color="blue", label="Min Temp.")
pres_line = ax_pres.plot(dates, pressure, linestyle="-", color="blue", label="Mean SLP")

# Add legend, title, labels
ax_temp.legend()
ax_pres.legend()
ax_temp.set_title("Time Series of Daily Temperature and Pressure in Jan 2017 at HKO")
ax_pres.set_xlabel("Date")
ax_temp.set_ylabel("Temperature (deg C)")
ax_pres.set_ylabel("Pressure (hPa)")

# Adjust x-ticks
date_fmt = mdates.DateFormatter("%m/%d")
ax_temp.xaxis.set_major_formatter(date_fmt)
date_interval = mdates.DayLocator(interval=5)
ax_temp.xaxis.set_major_locator(date_interval)
ax_temp.set_xlim(pd.datetime(2017,1,1), pd.datetime(2017,1,31))

# Save the output
fig.savefig("Jan2017.png",dpi=300)



