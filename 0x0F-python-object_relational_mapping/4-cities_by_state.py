#!/usr/bin/python3
"""A script that prints the list of all cities in a database"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
