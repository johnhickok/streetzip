#!/usr/bin/python
# -*- coding: utf-8 -*-

# sample_unidecode.py cleans out non-utf8 characters and replaces them with utf8. PostGIS is
# sensitive; this step is extremely helpful. More info on the Python modules used are in the README.

from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

# Each line of your infile_csv contains street names and coordinates from OpenStreeMap.
# The output is converted to a shapefile or you can modify this script for parsing
# direcly into PostGIS.

infile_csv = open('roads.csv', 'r')
outfile_csv = open('lineWKT.csv', 'w')

for s in infile_csv:
    outfile_csv.write(remove_non_ascii(s))
  
infile_csv.close()
outfile_csv.close()
