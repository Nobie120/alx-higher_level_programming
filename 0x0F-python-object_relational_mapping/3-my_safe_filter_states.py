#!/usr/bin/python3
""" safe pattern search """

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
                f"Usage: {sys.argv[0]} < username >
                < password > < database > < statename >")
        sys.exit(1)

    db = MySQLdb.connect(
            host='localhost', user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
    match = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
