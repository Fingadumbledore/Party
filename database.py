import sqlite3

def dbcon():
    con = sqlite3.Connection("party.db")
    cur = con.cursor()
    
def create_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("CREATE TABLE messages (username text, message text, timestamp text)")
    conn.commit()
    conn.close()
