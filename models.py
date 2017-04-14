import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS table')
conn.close()
