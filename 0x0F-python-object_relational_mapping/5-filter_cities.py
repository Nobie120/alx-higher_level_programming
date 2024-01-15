#!/usr/bin/python3
"""  takes in the name of a state as an
argument and lists all cities of that state """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
                ON states.id=cities.state_id WHERE states.name=%s""",
                (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
