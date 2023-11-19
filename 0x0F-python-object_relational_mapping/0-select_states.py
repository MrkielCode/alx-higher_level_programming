#!/usr/bin/python3
"""
script to list name of state

"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    my_user = argv[1]
    my_password = argv[2]
    my_db = argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=my_user,
        passwd=my_password,
        db=my_db
    )

    cur = conn.cursor()
    statement = 'SELECT name FROM states ORDER BY id ASC'
    cur.execute(statement)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
