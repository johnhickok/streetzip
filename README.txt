Streets + Zip Codes Data Search

Our staff of county workers is small, and our geocoding tasks are large, therefore we utilize every tool we can to get the work done. One our methods utilizes a database of current street names to verify and correct typos we find.

A simple Python script (streetzip.py) accesses a sqlite database (streetz.db) containing statewide California street names and their corresponding ZIP Codes.

streetlist.txt contains output from streetzip.py.

CreatingStreetZipSqlite.txt explains the steps it takes to create streetz.db from OpenStreetMap data. This how-to is a work in progress, but there's enough to get you going. I'm polishing it as I have time.

sample_unidecode.py was used to replace non-utf-8 characters from your OSM data before geoprocessing with PostGIS.

summary.zip contains a csv file containing the same street names, counts of street names, and corresponding zip codes that are in streetz.md. Some people just want raw data, so here is a copy.

jhickok2011@gmail.com, 2016-06-01
