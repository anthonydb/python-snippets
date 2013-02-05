# Generate JSON from a SQL database
# Requires pyodbc or other database connector (psycopg2, etc.)
# Subject of blog post at:
# http://www.anthonydebarros.com/2012/03/11/generate-json-from-sql-using-python/

import pyodbc
import json
import collections

# Set database connection
connstr = 'DRIVER={SQL Server};SERVER=ServerName;DATABASE=Test;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

# Query database table
cursor.execute("""
            SELECT ID, FirstName, LastName, Street, City, ST, Zip
            FROM Students
            """)
rows = cursor.fetchall()

# Convert query to row arrays
rowarray_list = []
for row in rows:
    t = (row.ID, row.FirstName, row.LastName, row.Street,
         row.City, row.ST, row.Zip)
    rowarray_list.append(t)

j = json.dumps(rowarray_list)
rowarrays_file = 'student_rowarrays.js'
f = open(rowarrays_file, 'w')
print >> f, j

# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['id'] = row.ID
    d['FirstName'] = row.FirstName
    d['LastName'] = row.LastName
    d['Street'] = row.Street
    d['City'] = row.City
    d['ST'] = row.ST
    d['Zip'] = row.Zip
    objects_list.append(d)

j = json.dumps(objects_list)
objects_file = 'student_objects.js'
f = open(objects_file, 'w')
print >> f, j

conn.close()
