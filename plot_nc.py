import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs #used to create map plot objects
import pandas as pd
import numpy as np

# Extract the data
data = xr.open_dataset("sfctemp.nc")
date = pd.datetime(2017,2,15)
lat = data["lat"]
lon = data["lon"]
temp = data["tempsfc"].loc[{"time": date}]

# Create map object
fig = plt.figure()

# Try changing the projection to PlateCarree and the value of central longitude
ax_map = fig.add_subplot(1,1,1, projection=ccrs.Mollweide(central_longitude=0.0))
ax_map.coastlines()

# Draw the color mesh plot
# Remove the whiteline along Prime Meridian by extending the temp array to 360.0
from cartopy.util import add_cyclic_point
temp, lon = add_cyclic_point(temp, coord=lon)
cmesh = ax_map.pcolormesh(lon, lat, temp, transform=ccrs.PlateCarree(), cmap="RdBu_r")

# Create lat/lon gridlines
gl = ax_map.gridlines(crs=ccrs.PlateCarree(), linestyle='--')

## Optional
#import matplotlib.ticker as mticker
#gl.xlocator = mticker.FixedLocator(np.linspace(-180, 180, 9))
#
## Zoom-in
#ax_map.set_extent([-45, 45, -70, 70])
#
## Range of colorbar
#cmesh.set_clim([250, 280])

fig.savefig("plot_nc.png",dpi=300)


