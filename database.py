import sqlite3
import json

def dbcon(sql):
    con = sqlite3.Connection("party.db")
    cur = con.cursor()
    cur.execute(sqlt)
    con.commit()

def return_dbcon(sql):
        try:
            con = sqlite3.connect("party.db")
            cur = con.cursor()
            ergebnis = cur.execute(sql).fetchall()
            con.commit()
            return ergebnis
        except:
            return "Error"

def mate_erstellen():
    try:
        with open('./Config/mate.json') as f:
            data = json.load(f)

        con = sqlite3.connect('party.db')
        cur = con.cursor()

        for mate in data:
            cur.execute('''INSERT INTO mate(mateid, matename, mateanzahl, kofein)
                        VALUES(?, ?, ?, ?)''',
                        (mate['id'], mate['name'], mate['anzahl'], mate['konfein']))
        con.commit()
        cur.close()
        con.close()
    except:
        print("Fehler beim laden der Datei: mate.json")

def create_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("CREATE TABLE messages (username text, message text, timestamp text)")
    conn.commit()
    conn.close()
