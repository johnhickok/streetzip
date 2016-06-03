CREATE A DATABASE OF UNIQUE STREET NAMES FROM OPEN STREETMAP

To get a list of streetnames and zipcodes, you will need to follow these steps.

1. GIS DATA DOWNLOADS

Download the statewide OPenStreetMap (OSM) shapefile, with thanks to Geofabrik
https://www.geofabrik.de/data/download.html

A statewide shapefile of zipcodes can be downloaded from Esri as a layer package (lpk) file.
https://www.arcgis.com/home/item.html?id=8d2012a2016e484dafaac0451f9aea24
A statewide shapefile can be extracted from this lpk file, but you'll need ArcGIS to do it.

2. CLEANUP OSM ROADS SHAPEFILE
The first part can be easily done with QGIS, but exercize patience if your state is large.

Add roads.shp to QGIS.

Remove all fields except (street) name.

Select and delete all the features that don't have any street names.

Simplify the geometry of your street features. Selecting 0.0002 degrees of arc as a minimum distance between nodes is about 80 feet and will reduce your node-load to around 25% of what you started with.

Extract Nodes to create a points shapfefile containing streetnames for every vertex of every roads feature.

3. USE PYTHON TO CLEAN UP NON UTF-8 CHARACTERS.
Numerous street names in OSM contain special characters that are outside many charcter sets, including LATIN-1. These special characters wreak havock while working with PostGIS, so this step was added.

Use QGIS to save your OSM points to a comma separated text (csv) file.

You will need to create a Python script to iterate through all the lines of your csv file. The Unidecode library converts characters like ñ to n, etc.

More info on the Unidecode library, visit
https://pypi.python.org/pypi/Unidecode

To install the unidecode library, you will need to install the latest version of pip,
https://pypi.python.org/pypi/pip

then ask pip to install the unidecode library, then, in your shell running Python, enter

pip install unidecode

Your script can look something like this:

#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

infile_csv = open('infile.csv', 'r')
outfile_csv = open('outfile.csv', 'w')

for s in infile_csv:
    outfile_csv.write(remove_non_ascii(s))
  
infile_csv.close()
outfile_csv.close()


Once your output csv file is cleaned, create a new points shapefile in QGIS.

4. USE POSTGIS
The next steps assumes the reader is familiar with PostGIS. If not, an abundance of online help is available. This workshop, provided by Boundless, is a favorite of many!
http://workshops.boundlessgeo.com/postgis-intro/

Use pgAdmin to set up your database.

Use pgShapeLoader to load your shapefiles into PostGIS. Note your WKID is still likely 4326.

Upon loading everything correctly, enter the following query into pgAdmin's SQL Editor:


SELECT 
osm_pts.name AS st_name,
COUNT(osm_pts.name) as st_count,
zip_codes.zip_code AS zip
FROM zip_codes
JOIN osm_pts
ON ST_Contains(zip_codes.geom, osm_pts.geom)
GROUP BY osm_pts.name, zip_codes.zip_code
ORDER BY osm_pts.name
;


The above assumes the shapefiles you loaded into PostGIS were osm_pts for your OSM roads points and zip_codes for your zip code polygons. A count of street name and zip code pairs was added as a quality check for your data.

Use pgAdmin to extract a csv file from your spatial query's results.

CREATE A SQLITE DATABASE WITH YOUR STREETS
Sqlite3 is free and in the public domain. Yiou can download a copy at .sqlite.org.


