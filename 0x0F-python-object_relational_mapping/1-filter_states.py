#!/usr/bin/python3
"""
1-select_states - lists all states from the database hbtn_0e_0_usa
with a name starting with N (upper N).
username, password and database will be passed as arguments to the
script
"""
if __name__ == "__main__":

    import MySQLdb
    import sys
    usr = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passw, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
