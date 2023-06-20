#!/usr/bin/python3
"""
This scripts list all the states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    """
    This connect the database and executes all the queries it intended to do
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
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
