# streetzip.py queries the streetz.db sqlite database and appends a list of zipcodes
# and street names into streetlist.txt. The streetz.db file contains an indexed list
# of street names and zipcodes extracted from OpenStreetMap data for California.
# Methods and data sources are in the REAME.

import webbrowser
import sqlite3

# Ask for user input in the CMD Console
print "This program gives you a list of streets in a given California Zip Code\n"
user_zip = raw_input( "Enter Zip Code:  " )
user_street = raw_input( "Enter Part of Street Name:  " )
user_city = raw_input( "Enter Part of City:  " )
print ""

# Open streetlist.txt
streetlist_file = open("streetlist.txt", "w")
streetlist_file.write("STREET, CITY, ZIP, VERTEX COUNT\n")

# parse a query search string qsearch and iterate database output into streetlist.txt
c = sqlite3.connect('streetz.db')
qsrch = "SELECT [st_name], [community], [zip], [st_count] FROM streetz WHERE zip like '%" + user_zip + "%' AND st_name like '%" + user_street + "%' AND community like '%" + user_city + "%' ORDER BY [st_name], [zip]"
for row in c.execute(qsrch):
  streetlist_file.write(str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + " | " + str(row[3]) + "\n")

streetlist_file.close()

# Display streetlist.txt
webbrowser.open("streetlist.txt")
