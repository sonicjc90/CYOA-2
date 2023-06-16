from unicodedata import name
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import requests
import database_info as db
from game import Game, Room

app = Flask(__name__)
game = None

@app.route('/', methods= ['GET'])
def index():
    # players = db.get_all_data()

    room = game.location
    game.set_maps(room)

    return render_template('room.html', room = room) 

# @app.route('/start-game', methods=['POST'])
# def start_game():
#     # Get form input
#     name = request.form['username']
#     gender = request.form['gender']
#     db.add_data(name, gender, None, None)
    
#     return redirect(url_for('/play'))

# @app.route('/player')
# def player():

#     return render_template('player.html')

# @app.route('/play')
# def play():
#     room = game.location
#     game.set_maps(room)

#     return render_template('room.html', room = room )


@app.route('/right', methods= ['GET'])
def right():
    game.go_right()
    return redirect(url_for('/play'))


@app.route('/left', methods= ['GET'])
def left():
    game.go_left()
    return redirect(url_for('/play'))
    


@app.route('/up', methods= ['GET'])
def up():
    game.go_top()
    return redirect(url_for('/play'))
    


@app.route('/down', methods= ['GET'])
def down():
    game.go_down()
    return redirect(url_for('/play'))
    

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')