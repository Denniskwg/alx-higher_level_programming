#!/usr/bin/python3
"""
4-cities_by_state - lists all cities
from the database hbtn_0e_4_usa
username, password and database will be passed as arguments to the
script
"""
if __name__ == "__main__":

    import MySQLdb
    import sys
    usr = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    sql = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities
         ON states.id = cities.state_id
         ORDER BY cities.id ASC
         """
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passw, db=db)
    cur = db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
