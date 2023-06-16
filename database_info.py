import sqlite3

database = './static/data/player-info.db'
# table: save_data

def delete_data(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("DELETE FROM save_data WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def update_data(Name, Gender, Room, Items, rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("UPDATE save_data Name = ?, Gender = ?, Rooms = ?, Items = ? WHERE rowid = ?", (Name, Gender, Room, Items, rowid))
    conn.commit()
    conn.close()


def add_data(Name, Gender, Room, Items):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO save_data (Name, Gender, Room, Items) VALUES (?, ?, ?, ?)", (Name, Gender, Room, Items))
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
            'Gender': row[2],
            'Room': row[3],
            'Items': row[4],
            'rowid': row[0]

        }
        post.append(post)
        conn.close()
    return posts