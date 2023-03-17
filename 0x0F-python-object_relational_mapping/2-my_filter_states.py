#!/usr/bin/python3
"""
2-my_filter_states - lists all states from the database hbtn_0e_0_usa
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
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=usr, passwd=passw, db=db)
    cur = db.cursor()
    cur.execute("SELECT \
        * FROM states WHERE name = '{}' ORDER BY id ASC;".format(name))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
