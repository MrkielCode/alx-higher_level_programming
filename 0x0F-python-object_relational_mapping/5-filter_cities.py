#!/usr/bin/python3

"""
script to list cities
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    statement = '''
    SELECT cities.name \
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id ASC
    '''

    cur.execute(statement, (argv[4], ))
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
