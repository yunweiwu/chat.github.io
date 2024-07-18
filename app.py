from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('chat.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            return redirect(url_for('chat', username=username))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/chat/<username>', methods=['GET', 'POST'])
def chat(username):
    if request.method == 'POST':
        message = request.form['message']
        conn = sqlite3.connect('chat.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (sender, content) VALUES (?, ?)", (username, message))
        conn.commit()
        conn.close()
        return redirect(url_for('chat', username=username))
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    messages = c.fetchall()
    conn.close()
    return render_template('chat.html', username=username, messages=messages)

if __name__ == '__main__':
    app.run(debug=True,port=4444)
