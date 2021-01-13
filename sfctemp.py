import xarray as xr
import numpy as np
import datetime as dt
  
# open file
data = xr.open_dataset("sfctemp.nc")
print(data["tempsfc"])
print(data.dims)
print(data.coords)
print(data.coords["lat"])
print(data.variables)

# attributes
print(data["tempsfc"].attrs)
print(data["tempsfc"].attrs["units"])
minT = data["tempsfc"].attrs["valid_range"][0]
maxT = data["tempsfc"].attrs["valid_range"][1]
print(minT, maxT)

# subscript
print(data["tempsfc"][2:6, 3, 4:9:2]) # index
print(data["tempsfc"][{"time":range(2,6),"lat":3,"lon":range(4,9,2)}]) # index
print(data["tempsfc"].loc[{"time":"2017-01-01T12:00:00", "lat": 80.0, "lon": np.arange(15.0, 25.0, 2.5)}])
print(data["tempsfc"][{"time":2, "lat":4, "lon":6}])

# modify values
data["tempsfc"][{"time":2, "lat":4, "lon":6}] = 250
data["tempsfc"].loc[{"time":"2017-01-01T12:00:00", "lat": 80.0, "lon": 15.0}] = 250
print(data["tempsfc"][{"time":2, "lat":4, "lon":6}])

# extract values (certain lat/lon)
lon_c = data["lon"]
lat_c = data["lat"]
required_lon = lon_c[np.logical_and(40.0 <= lon_c, lon_c <= 50.0)] # [40.0 42.5 45.0 47.5 50.0]
required_lat = lat_c[lat_c <= 10.0] # [10.0 7.5 5.0 2.5 0.0 ... -82.5 -85.0 -87.5 -90.0]
print(data["tempsfc"].loc[{"time":"2017-01-01T12:00:00", "lat":required_lat, "lon":required_lon}])

# extract values (certain time)
start = dt.datetime(year=2017, month=1, day=28)
end   = dt.datetime(year=2017, month=2, day=4)
date_list = [start + dt.timedelta(days=x) for x in range(0, (end-start).days)]
for date in date_list:
    print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(data.loc[{"time":date_list}])


