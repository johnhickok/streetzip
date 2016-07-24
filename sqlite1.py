import sqlite3
c = sqlite3.connect('.\\test1.db')
c.execute("CREATE TABLE streetz (st_name text, community text, zip text, st_count integer);")

"""

sqlite3 command line functions:
CREATE TABLE streetz (st_name text, community text, zip text, st_count integer);
.separator '|'
.import streetz.csv streetz
CREATE INDEX streetz_index on streetz (st_name, zip);
.quit


better solution:
http://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python

import csv, sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);")

with open('data.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()


see also:
import csv, sqlite3
conn = sqlite3.connect("pcfc.sl3")
curs = conn.cursor()
curs.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
reader = csv.reader(open('PC.txt', 'r'), delimiter='|')
for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
conn.commit()


"""