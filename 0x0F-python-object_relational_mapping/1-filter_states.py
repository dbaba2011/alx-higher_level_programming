#!/usr/bin/python3
"""Lists all the states with a name starting with N from the hbtn_0e_i_usa"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306,
                           password=argv[2], user=argv[1], db=argv[3])
    cur = conn.cursor()
    cur.execute(" select * from states where name LIKE'N%' ORDER BY id ASC;")
    result = cur.fetchall()
    for row in result:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
