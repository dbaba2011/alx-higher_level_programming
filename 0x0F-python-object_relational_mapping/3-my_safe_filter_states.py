#!/usr/bin/python3
"""
A script should take 4 arguments:
mysql username, mysql password,
database name and state name searched
(safe from MySQL injection)
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                ('%' + name + '%',))
    result = cur.fetchall()
    for row in result:
        if row[1] == name:
            print(row)
    cur.close
    conn.close
