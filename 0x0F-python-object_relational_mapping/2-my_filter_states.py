#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
              LIKE '{:s}' ORDER BY id ASC"""
              .format(argv[4]))
    rows = c.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    c.close()
    db.close()
