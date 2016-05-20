from flask import Flask, redirect, url_for, request
from flask import render_template
import sqlite3
import ORM

app = Flask(__name__)

@app.route('/')
def index():
    ORM.query_DB.create_user()
    return render_template('index.html')

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0')
