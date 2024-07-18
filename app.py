from flask import Flask, render_template, request, jsonify, g
import sqlite3
import hashlib

app = Flask(__name__)
DATABASE = 'chat.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cur.fetchone()
    if user:
        return jsonify({'success': True, 'username': username})
    else:
        return jsonify({'success': False})

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    db.commit()
    return jsonify({'success': True})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM messages")
    messages = cur.fetchall()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
