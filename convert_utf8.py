#!/usr/bin/python
# -*- coding: utf-8 -*-

# convert_utf8.py inputs roads_wkt.csv and outputs roads_wkt_utf8.csv, containing only wkt and name fields.
# It also replaces any special charcters with utf-8 characters usng the unidecode module. Note the unidecode
# module is not included with standard Python; see https://pypi.python.org/pypi/Unidecode

import csv
from unidecode import unidecode

# set up your unidecode function
def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

infile_csv = open('roads_wkt.csv', 'r')
outfile_csv = open('roads_wkt_utf8.sql', 'w')

#outfile_csv.write('WKT,name\n')

with open('roads_wkt.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row['name'] > '':
            new_row = "INSERT INTO roads(name, geom) VALUES ('" + remove_non_ascii(row['name']) + "',ST_GeomFromText('" + row['WKT'] + "',4326));\n"
            outfile_csv.write(new_row)

infile_csv.close()
outfile_csv.close()

