""" database stuff """
import sqlite3
import json
from log import insert_log

def dbcon(sql: str):
    """ Execute given SQL-Command """
    try:
        con = sqlite3.Connection("party.db")
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    except Exception as e:
        print(f"Fehler: {e}")

def return_dbcon(sql):
        """ connext to database and return stuff """
        try:
            con = sqlite3.connect("party.db")
            cur = con.cursor()
            ergebnis = cur.execute(sql).fetchall()
            con.commit()
            return ergebnis
        except Exception as e:
            insert_log(file="server", data=f"Error: {e}", log_type="ERROR")
            insert_log(file="server", data=f"Error: {e}", log_type="ERROR")


def mate_erstellen():
    """ collect mate data from json """
    try:
        with open('./Config/mate.json') as f:
            data = json.load(f)

        con = sqlite3.connect('party.db')
        cur = con.cursor()

        for mate in data:
            cur.execute('''INSERT INTO mate(mateid, matename, mateanzahl, kofein)
                        VALUES(?, ?, ?, ?)''',
                        (mate['id'], mate['name'], mate['anzahl_pro_kasten'], mate['koffein']))
        con.commit()
        cur.close()
        con.close()
    except:
        print("Fehler beim laden der Datei: mate.json")

def create_db():
    """ a little bit useless """
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("CREATE TABLE messages (username text, message text, timestamp text)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Use main.py to use program")
