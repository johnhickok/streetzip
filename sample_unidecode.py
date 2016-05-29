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
