#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
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
    cmd = ("SELECT cities.id, cities.name, states.name FROM states "
           "JOIN cities ON states.id = cities.state_id WHERE states.name = %s "
           "ORDER BY cities.id ASC;")
    param = (sys.argv[4],)
    cursor.execute(cmd, param)
    rows = cursor.fetchall()

    names = [row[1] for row in rows]
    print(", ".join(names))

    cursor.close()
    conn.close()
