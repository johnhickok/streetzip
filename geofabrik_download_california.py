# geofabrik_download_california.py downloads OpenStreetMap data from GeoFabrik for California

# Import system modules
import urllib, os, zipfile

current_folder = os.getcwd()

url_zip = 'http://download.geofabrik.de/north-america/us/california-latest.shp.zip'
download = 'california-latest.zip'

# Extract everything in the archive
urllib.urlretrieve(url_zip, download)
with zipfile.ZipFile(download, "r") as z:
    z.extractall(current_folder)

# Remove other files except roads
other_files = ['buildings', 'landuse', 'natural', 'places', 'points', 'railways', 'waterways']

for file in other_files:
    extensions = ['cpg', 'dbf', 'prj', 'shp', 'shx']
    for ext in extensions:
        os.remove(current_folder + "\\" + file + "." + ext)
