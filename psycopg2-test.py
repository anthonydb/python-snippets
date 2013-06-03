# basic connection to postgres with psycopg2

import psycopg2

conn = psycopg2.connect("host=localhost dbname=mydatabase user=username password=mypassword")
cur = conn.cursor()

cur.execute("INSERT INTO table_name VALUES (1,'some text',21,12)")
conn.commit()

cur.close()
conn.close()

