#!/usr/bin/python3
"""
5-filter_cities - lists all cities
from the database hbtn_0e_4_usa where state is equal to passed
argument
username, password and database will be passed as arguments to the
script
"""
if __name__ == "__main__":

    import MySQLdb
    import sys
    usr = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    sql = """SELECT cities.name, states.name
         FROM states
         INNER JOIN cities
         ON states.id = cities.state_id
         WHERE states.name = %s
         ORDER BY cities.id ASC
         """
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passw, db=db)
    cur = db.cursor()
    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i < len(rows) - 1:
            if rows[i][1] == sys.argv[4]:
                print("{}, ".format(rows[i][0]), end="")
        else:
            if rows[i][1] == sys.argv[4]:
                print(rows[i][0])
    cur.close()
    db.close()
