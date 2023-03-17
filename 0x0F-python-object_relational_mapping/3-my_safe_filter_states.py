#!/usr/bin/python3
"""
3-my_safe_filter_states - lists all states
from the database hbtn_0e_0_usa where name matches passed arg
username, password and database will be passed as arguments to the
script
"""
if __name__ == "__main__":

    import MySQLdb
    import sys
    usr = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    sql = """SELECT *
         FROM states
         WHERE name = %s
         ORDER BY id ASC
         """
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passw, db=db)
    cur = db.cursor()
    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
