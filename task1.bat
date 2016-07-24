echo begin task 1 >> log1.txt
echo %time% >> log1.txt

python geofabrik_download_california.py
echo downloaded california-latest.zip >> log1.txt
echo %time% >> log1.txt

call "C:\Program Files\QGIS Essen\bin\o4w_env.bat"
echo set up osgeo4w environment >> log1.txt
echo %time% >> log1.txt

ogr2ogr -f CSV roads_wkt.csv roads.shp -lco GEOMETRY=AS_WKT
echo converted shp to csv >> log1.txt
echo %time% >> log1.txt

del california-latest.zip
echo deleted california-latest.zip >> log1.txt
echo %time% >> log1.txt
