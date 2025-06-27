#!/usr/bin/python3
"""
Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections.
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
    cmd = ("SELECT * FROM states WHERE name = %s "
           "ORDER BY states.id ASC;")
    param = (sys.argv[4],)
    cursor.execute(cmd, param)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
