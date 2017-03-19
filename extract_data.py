# extract_data.py extracts the table streetz from the SQLite database into file streetz.csv.

import sqlite3

# Open streetz.txt 
streetlist_file = open("streetz.csv", "w")

# parse a query search string qsearch and iterate database output into streetlist.txt
c = sqlite3.connect('streetz.db')
qsrch = "SELECT * FROM streetz"
for row in c.execute(qsrch):
  streetlist_file.write(str(row[0]) + "|" + str(row[1]) + "|" + str(row[2]) + "|" + str(row[3]) + "|\n")

streetlist_file.close()
