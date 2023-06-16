#!/usr/bin/python3
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db")
c = conn.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
rows = cur.fetchall()
for row in rows:
    print(row)
c.close()
conn.close()
