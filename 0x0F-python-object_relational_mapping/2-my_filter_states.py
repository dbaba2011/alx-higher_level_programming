#!/usr/bin/python3
""" This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name ='{:s}' ORDER BY id ASC"
                .format(name,))
    result = cur.fetchall()
    for row in result:
        if row[1] == name:
            print(row)
    cur.close
    conn.close
