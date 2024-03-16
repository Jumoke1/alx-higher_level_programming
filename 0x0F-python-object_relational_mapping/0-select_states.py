#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

<<<<<<< HEAD
db = MYSQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

cur = bd.cursor()
cur.execute("SELECT * FROM states")

rows = cur.fetchall()
=======
db = SQL.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()

>>>>>>> e2ffc548ac0aa236d1d41b8e3b6c5ccc76952866
for row in rows:
    print(row)
