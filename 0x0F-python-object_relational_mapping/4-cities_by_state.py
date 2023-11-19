#!/usr/bin/python3

"""
script to list cities
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    statement = '''
    SELECT cities.id, cities.name, states.name
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC
    '''

    cur.execute(statement)
    rows = cur.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    cur.close()
    conn.close()
