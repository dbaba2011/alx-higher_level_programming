#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""
if __name__ == "__main__":
    """
    This connect to the database and execute all queries it designs to perform
    """

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host="localhost",
        user=f"{argv[1]}",
        password=f"{argv[2]}",
        db=f"{argv[3]}",
        port=3306,
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' \
                ORDER BY states.id ASC".format(argv[4])
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
