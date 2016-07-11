python geofabrik_download_california.py

call "C:\Program Files\QGIS Essen\bin\o4w_env.bat"

ogr2ogr -f CSV roads_wkt.csv roads.shp -lco GEOMETRY=AS_WKT

del california-latest.zip
