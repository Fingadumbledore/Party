import sqlite3

conn = sqlite3.connect("chat.db")
c = conn.cursor()
c.execute("CREATE TABLE messages (username text, message text, timestamp text)")
conn.commit()
conn.close()
