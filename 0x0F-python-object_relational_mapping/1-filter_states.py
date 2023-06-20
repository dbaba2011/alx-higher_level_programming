#!/usr/bin/python3
"""
This scripts list all the states starting with the N from the database hbtn_0e_0_usa and return them as a tuple.
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
    cur.execute("SELECT * FROM states Where name LIKE 'N%' ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
