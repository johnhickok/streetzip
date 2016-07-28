# make_sqlite_db.py creates sqlite database streetz.db from csv file streetz.csv
# More help on importing csv files into sqlite can be found at:
# http://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python

import csv, sqlite3
c = sqlite3.connect('.\\test1.db')
c.execute("CREATE TABLE streetz (st_name text, community text, zip text, st_count integer);")

reader = csv.reader(open('streetz.csv', 'r'), delimiter='|')
for row in reader:
    to_db = [row[0], row[1], row[2], row[3]]
    # to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    c.execute("INSERT INTO streetz (st_name, community, zip, st_count) VALUES (?, ?, ?, ?);", to_db)
    # curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
c.commit()
