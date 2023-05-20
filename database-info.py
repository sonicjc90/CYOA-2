import sqlite3

database = './static/data/player-info.db'
# table: save_data

def delete_data(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("DELETE FROM save_data WHERE rowid = ?", (Name, Room, Items))
    conn.commit()
    conn.close()

def update_data(Name, Room, Items):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("UPDATE", (Name, Room, Items))
    conn.commit()
    conn.close()


def add_data(Name, Room, Items):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO save_data (Name, Room, Items) VALUES (?, ?, ?)", (Name, Room, Items))
    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM save_data")
    posts = []
    for row in result: 
        post = {
            'Name': row[1],
            'Room': row[2],
            'Items': row[3],
            'rowid' : row[0]

        }
        post.append(post)
        conn.close()
    return posts