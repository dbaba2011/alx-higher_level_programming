#!/usr/bin/python3
"""
This script that lists all cities from the database hbtn_0e_4_usa
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
        "SELECT cities.id ,cities.name, states.name from cities inner join states on state_id = states.id ORDER BY cities.id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
