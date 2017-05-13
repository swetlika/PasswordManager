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

def insert(domain,username,password, iv):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pm (domain,username,password,iv) VALUES (?,?,?,?)", (domain,username,password,iv))
    con.commit()
    con.close()
    
def retrieveAll(master):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT domain,username,password,iv FROM pm")
    table = cur.fetchall()
    con.close()
    return [(xstr(row[0]), xstr(row[1]), xstr((enc.decrypt_msg(row[2], xstr(master).encode('utf-8'), row[3])).decode('utf-8'))) for row in table]

def retrieve(url):
    con = sql.connect("database.db")
    cur = con.cursor()
    domain = urlparse(url).hostname
    cur.execute("SELECT username, password,iv from pm where domain='{dm}'".\
      format(dm=domain))
    table = cur.fetchall()
    con.close()
    row = table[0]
    return xstr(row[0]), xstr((enc.decrypt_msg(row[1], xstr(master).encode('utf-8'), row[2])).decode('utf-8'))


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        master = request.form['master']
        url = request.form['domain']
        username = request.form['username']
        password = request.form['password']

        domain = urlparse(url).hostname
        iv, encrypted_pw = enc.encrypt_msg(xstr(password).encode('utf-8'),xstr(master).encode('utf-8'))

        insert(domain, username, encrypted_pw, iv)
        #table = retrieveAll()
        #return render_template('index.html',table=table)
    else:
        return render_template('fail.html')

@app.route('/table', methods=['POST', 'GET'])
def table():
    if request.method=='POST':
        master_pw = request.form['master_pw']
        
        if enc.master_check(master_pw.encode('utf-8')):
          table = retrieveAll(master_pw)
          return render_template('index.html',table=table)
        return render_template('fail.html')

@app.route('/test', methods=['POST','GET'])
def test():
    if request.method=='GET':
      master_pw = request.args.get('master_pw');
      #replace with proper master pw check with decrypt
      if not enc.master_check(master_pw.encode('utf-8')):
        return jsonify({
          "status":"fail"
          })

      url = request.args.get('url');
      userpass = retrieve(url)
      username = userpass[0]
      password = userpass[1]

      return jsonify({
        "status":"success",
        "username": username,
        "password": password
        })
#@app.route('/', methods=['POST', 'GET'])
#def view_passwords():
#    dbHandler.insert(domain, username, password)
#    table = dbHandler.retrieveAll()
#    return render_template('index.html', table=table)
    
if __name__ == "__main__":
    app.run(debug = True)
