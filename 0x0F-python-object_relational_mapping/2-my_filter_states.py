#!/usr/bin/python3
""" searching for a specific name values """

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} <username> <password> <database> <rows>")
        sys.exit(1)

    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
            """SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY id ASC""".format(sys.argv[4]))
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
