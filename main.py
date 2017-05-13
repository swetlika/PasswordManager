from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
from schema import *
import random, string
import enc_functions as enc
from urllib.parse import urlparse

conn = sql.connect('database.db')
app = Flask(__name__)

def xstr(s):
    if s is None:
        return ''
    return str(s)

master = 'master' #get it from input

def master_check(master_pw):
    hash = hash_pash(master_pw)
    return hash=="FC613B4DFD6736A7BD268C8A0E74ED0D1C04A959F59DD74EF2874983FD443FC9"

def insert(domain,username,password, iv):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pm (domain,username,password,iv) VALUES (?,?,?,?)", (domain,username,password,iv))
    con.commit()
    con.close()
    
def retrieveAll():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT domain,username,password,iv FROM pm")
    table = cur.fetchall()
    print(table)
    con.close()
    return [(xstr(row[0]), xstr(row[1]), xstr((enc.decrypt_msg(row[2], xstr(master).encode('utf-8'), row[3])).decode('utf-8'))) for row in table]


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        #master = request.form['master']
        url = request.form['domain']
        username = request.form['username']
        password = request.form['password']

        domain = urlparse(url).hostname
        iv, encrypted_pw = enc.encrypt_msg(xstr(password).encode('utf-8'),xstr(master).encode('utf-8'))

        insert(domain, username, encrypted_pw, iv)
        table = retrieveAll()
        return render_template('index.html',table=table)
    else:
        table = retrieveAll()
        return render_template('index.html',table=table)


@app.route('/test', methods=['POST','GET'])
def test():
    if request.method=='GET':
        return jsonify({
        "username":"ray",
        "password":"test"
        })
#@app.route('/', methods=['POST', 'GET'])
#def view_passwords():
#    dbHandler.insert(domain, username, password)
#    table = dbHandler.retrieveAll()
#    return render_template('index.html', table=table)
    
if __name__ == "__main__":
    app.run(debug = True)
