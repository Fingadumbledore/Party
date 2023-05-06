import sqlite3

def dbcon():
    con = sqlite3.Connection("party.db")
    cur = con.cursor()

def return_dbcon(sql):
        try:
            con = sqlite3.connect("party.db")
            log_server("return_dbcon hat die Verbindung mit db aufgenommen", "WARNING")
            cur = con.cursor()
            ergebnis = cur.execute(sql).fetchall()
            con.commit()
            return ergebnis
        except:
            return "Error"

def create_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("CREATE TABLE messages (username text, message text, timestamp text)")
    conn.commit()
    conn.close()
