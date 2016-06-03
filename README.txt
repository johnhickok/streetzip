Streets + Zip Codes Data Search

Our staff of county workers is small, and our geocoding tasks are large, therefore we utilize every tool we can get our hands on to get the work done.

When analyzing addresses that have typos in street names, it helps to have a handy database of streets that are more correct.

This project uses a simple Python script streetzip.py to access a sqlite database streetz.db containing a total list of street names in California and the corresponding zip codes the streets were found in.

streetlist.txt contains output from streetzip.py. It's empty for now. You really don't need it - streetzip.py will overwrites this text file when your run it.

CreatingStreetZipSqlite.txt is a work in progress, going through the steps it takes to create streetz.db from OpenStreetMap data. This how-to is a work in progress, but there's likely enough in it to get you going. I'm polishing it as I have time.

sample_unidecode.py was used to replace non-utf-8 characters from your OSM data before geoprocessing with PostGIS.

summary.zip contains a csv file containing the same street names, counts of street names, and corresponding zip codes that are in streetz.md. Some people just want raw data, so here is a copy.

jhickok2011@gmail.com, 2016-06-01
