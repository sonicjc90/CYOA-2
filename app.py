from unicodedata import name
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import database_info as db
from game import Game, Room

app = Flask(__name__)
game = None
username = input('Type in Name Here: ')
user_gender = input('Choose your Gender: ')

@app.route('/', methods= ['GET'])
def index():

    return render_template('homepage.html') 

@app.route('/start-game', methods=['POST'])
def start_game():
    # Get form input
    name = ''
    gender = ''
    # Set player name & gender
    # Start new game
    game = Game(name, gender)
    return redirect(url_for('play'))

    

@app.route('/play')
def play():
    
    return render_template('room.html', room = game.location )

    


@app.route('/right', methods= ['GET'])
def right():
    game.go_right()
    return redirect(url_for('play'))


@app.route('/left', methods= ['GET'])
def left():
    game.go_left()
    return redirect(url_for('play'))
    


@app.route('/up', methods= ['GET'])
def up():
    game.go_up()
    return redirect(url_for('play'))
    


@app.route('/down', methods= ['GET'])
def down():
    game.go_down()
    return redirect(url_for('play'))
    

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')