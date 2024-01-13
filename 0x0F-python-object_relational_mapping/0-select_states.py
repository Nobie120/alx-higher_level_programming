#!/usr/bin/python3
""" the mysqldb module """

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database, charset='utf8'
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
