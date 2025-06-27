#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    cursor = conn.cursor()
    cmd = ("SELECT * FROM states WHERE name "
           "LIKE BINARY 'N%' "
           "ORDER BY states.id ASC;")
    cursor.execute(cmd)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
