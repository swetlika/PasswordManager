from flask import Flask, render_template, redirect, request, flash,g,session,url_for
import sqlite3 as sql
#from models import *

#conn = sqlite3.connect('database.db')
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return 'hello'

 
if __name__ == "__main__":
    app.run(debug = True)
