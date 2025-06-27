#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
    cmd = ("SELECT * FROM states WHERE name = '{}' "
           "ORDER BY states.id ASC;".format(sys.argv[4]))
    cursor.execute(cmd)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
