#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
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
    cmd = ("SELECT cities.id, cities.name, states.name "
           "FROM states "
           "JOIN cities ON states.id = cities.state_id "
           "ORDER BY cities.id ASC;")
    cursor.execute(cmd)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
