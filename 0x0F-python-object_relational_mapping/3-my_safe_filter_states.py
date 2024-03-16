#!/usr/bin/python3
"""Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!."""

import MySQLdb
import sys

if __name__ == '__main__':

db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY %(name)s \
        ORDER BY states.id".format(sys.arvg[4]))
rows = cur.fetchall()

for row in rows:
    print(row)
