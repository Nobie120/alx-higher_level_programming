#!/usr/bin/python3
""" Pattern matching """

import sys
import MySQLdb


if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <username> <password> <database>")
    sys.exit(1)

db = MySQLdb.connect(
        host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        port=3306
        )
cur = db.cursor()
cur.execute(
    """ 
    SELECT * FROM states WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC
    """
    )
result = cur.fetchall()
for row in result:
    print(row)

cur.close()
db.close()
