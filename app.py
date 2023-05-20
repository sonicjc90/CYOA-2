from unicodedata import name
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import database-info as db

app = Flask(__name__)

player = input("Please enter your name here ---> ").lower

@app.route('/', methods= ['GET'])
def index():
    
    if player == '':
        db.add_data(Name)

    return render_template('index.html') 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')