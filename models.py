import sqlite3 as sql

    
def insert(domain,username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pm (domain,username,password) VALUES (?,?,?)", (domain,username,password))
    con.commit()
    con.close()
    
def retrieveAll():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM pm")
	table = cur.fetchall()
	con.close()
	return table