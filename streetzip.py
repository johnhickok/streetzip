import webbrowser
import sqlite3

print "This program gives you a list of streets in a given California Zip Code\n"
user_zip = raw_input( "Enter Zip Code:  " )
user_street = raw_input( "Enter Part of Street Name:  " )
print ""

streetlist_file = open('streetlist.txt', 'w')

c = sqlite3.connect('streetz.db')
    
# parse a query search string qsearch
qsrch = "SELECT [st_name], [zip] FROM streetz WHERE zip like '%" + user_zip + "%' AND st_name like '%" + user_street + "%' ORDER BY [st_name]"

for row in c.execute(qsrch):
  streetlist_file.write(str(row[1]) + " " + str(row[0]) + "\n")

streetlist_file.close()

webbrowser.open('streetlist.txt')
