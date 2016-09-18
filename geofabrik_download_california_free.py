# geofabrik_download_california_free.py downloads OpenStreetMap data from GeoFabrik for California

# Import system modules
import urllib, os, zipfile

current_folder = os.getcwd()

#url_zip = 'http://download.geofabrik.de/north-america/us/california-latest.shp.zip'

url_zip = 'http://download.geofabrik.de/north-america/us/california-latest-free.shp.zip'
download = 'california-latest-free.zip'

# Extract everything in the archive
urllib.urlretrieve(url_zip, download)
with zipfile.ZipFile(download, "r") as z:
    z.extractall(current_folder)

# Remove other files except roads
other_files = ['gis.osm_buildings_a_free_1', 'gis.osm_landuse_a_free_1', 'gis.osm_natural_a_free_1', 'gis.osm_natural_free_1', 'gis.osm_places_a_free_1', 'gis.osm_places_free_1', 'gis.osm_pofw_a_free_1', 'gis.osm_pofw_free_1', 'gis.osm_pois_a_free_1', 'gis.osm_pois_free_1', 'gis.osm_railways_free_1', 'gis.osm_traffic_a_free_1', 'gis.osm_traffic_free_1', 'gis.osm_transport_a_free_1', 'gis.osm_transport_free_1', 'gis.osm_waterways_free_1', 'gis.osm_water_a_free_1']

for file in other_files:
    extensions = ['cpg', 'dbf', 'prj', 'shp', 'shx']
    for ext in extensions:
        os.remove(current_folder + "\\" + file + "." + ext)
