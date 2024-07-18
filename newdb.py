import sqlite3
import hashlib

DATABASE = 'chat.db'

def init_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, username TEXT, message TEXT)")
    hashed_password1 = hashlib.md5('123456'.encode()).hexdigest()
    hashed_password2 = hashlib.md5('123456'.encode()).hexdigest()
    cur.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('w', hashed_password1))
    cur.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('C', hashed_password2))
    db.commit()
    db.close()

init_db()
