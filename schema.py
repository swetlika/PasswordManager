import sqlite3 as sql

conn = sql.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS pm (domain TEXT, username TEXT, password TEXT)')
conn.close()