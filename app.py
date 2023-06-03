from unicodedata import name
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import database-info as db

app = Flask(__name__)

player = input("Please enter your name here ---> ").lower

class Room:
    def __init__ (self, name, tools, prompt)
    self.name = name 
    self.tools = tools
    self.prompt = prompt

ER = Room("Engine Room", "", "")
CF = Room("Cafeteria", "", "")
SP = Room("Spawn Point", "", "")
CC = Room("Control Center", "", "")
AR = Room("Airlock", "", "")
MB = Room("Medbay", "", "")
GA = Room("General Area", "", "")


room_dir =  {
    "top 1" : "Control Center",
    "top 2" :  "Cafeteria",
    "middle1" : "Airlock",
    "middle2" : "Medbay",
    "middle3" : "General Area",
    "bottom1" : "Spawn Point",
    "bottom2" : "Engine Room",
}

name = input("Please enter your name :")
print(name)

@app.route('/', methods= ['GET'])
def index():
    
    if player == '':
        db.add_data(Name)

    return render_template('index.html') 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')