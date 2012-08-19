# Example of using pyodbc to connect to server, fetch data,
# and return it as JSON or print to screen

# module import
import pyodbc
import json

# server-specific connection string
connstr = 'DRIVER={SQL Server};SERVER=ServerName;DATABASE=Test;'

# use pyodbc's "connect" method to establish the connection
conn = pyodbc.connect(connstr)

# create a cursor object using the connection's "cursor" method
cursor = conn.cursor()

# two variables to limit the query
fname = 'Bob'
lname = 'Jones'

# execute the query, passing in the variables
cursor.execute("""
            SELECT ID, LastName, FirstName
            FROM Employees
            WHERE LastName = ? AND FirstName = ?
            """, lname, fname)

# the variable "rows" contains every row fetched
rows = cursor.fetchall()

# now, build a list of lists to output to JSON
outlist = []
for row in rows:
    l = [row.FirstName, row.LastName, str(row.ID)]   
    outlist.append(l)
    #print row.FirstName + ' ' + row.LastName + ', ID: ' + str(row.ID) 

# dump the list to JSON and print to screen.
j = json.dumps(outlist)
print j

# close the connection to the server
conn.close()
