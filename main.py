from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import models as dbHandler

app = Flask(__name__)
    
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
   		domain = request.form['domain']
   		username = request.form['username']
   		password = request.form['password']
        
   		dbHandler.insert(domain, username, password)
   		table = dbHandler.retrieveAll()
   		return render_template('index.html',table=table)
    else:
   		return render_template('index.html')
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
