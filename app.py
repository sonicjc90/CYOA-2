from unicodedata import name
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import database-info as db
from game import Game

app = Flask(__name__)
game = None

@app.route('/', methods= ['GET'])
def index():
    # Welcome user
    # Enter name form 
    # Enter gender
    return render_template('index.html') 

@app.route('/start-game', methods=['POST'])
def start_game():
    # Get form input
    name = ''
    gender = ''
    # Set player name & gender
    # Start new game
    game = Game(name, gender)
    # redirect to play where game begins
    pass

@app.route('/play')
def play():
    # show current game location
    render_template('game.html', game.location )
    


@app.route('/right', methods= ['GET'])
def right():
    game.go_right()
    render_template('game.html', game.location )


@app.route('/left', methods= ['GET'])
def left():
    pass


@app.route('/up', methods= ['GET'])
def index():
    pass


@app.route('/down', methods= ['GET'])
def index():
    pass

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')