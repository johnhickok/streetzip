#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenAddress.py is a Python script that summarizes a unique list of street names with their asscociated 
# cities and zip codes from csv files you can download from the Open Address project (https://openaddresses.io/). 
# Download a region and place this script into a folder for the state you want. Note these large 
# regional downloads can take a while.

# Import modules
import os, csv, sqlite3

# Visit https://pypi.python.org/pypi/Unidecode to install this library
from unidecode import unidecode

# Set up your unidecode function.
def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

# Ge a list of CSV files in the current directory
mypath = os.getcwd()
csvlist = []
for f in os.listdir(mypath):
  if '.csv' in f:
    csvlist.append(f)

# For each CSV file, import only the attributes you need into in-memory sqlite database, 
# then select distinct streets, etc.
for file in csvlist:
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE t (STREET, CITY, POSTCODE);")

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        to_db = [(remove_non_ascii(i['STREET']), remove_non_ascii(i['CITY']), i['POSTCODE']) for i in reader]

    cur.executemany("INSERT INTO t (STREET,CITY,POSTCODE) VALUES (?, ?, ?);", to_db)
    con.commit()

    newfilename = 'new\\' + file
    newfile = open(newfilename, 'w')

    for row in cur.execute("SELECT DISTINCT * FROM t WHERE STREET > '' ORDER BY STREET, CITY, POSTCODE"):
        newfile.write(row[0] + "," + row[1] + "," + row[2] + '\n')

    con.close()


