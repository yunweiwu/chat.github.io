import sqlite3
conn = sqlite3.connect('chat.db')
c = conn.cursor()
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('w', '123456'))
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('C', '123456'))
conn.commit()
conn.close()
