#!/usr/bin/python3
"""
script to list name of state

"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = conn.cursor()
    statement = """SELECT name FROM states ORDER BY id"""
    cur.execute(statement)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
