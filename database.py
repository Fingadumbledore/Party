import os, sys, sqlite3

def creat_stand_db():
    if os.path.exists("stand.db"):
        print("stand.db bereits vorhanden")
        
    else:
        # Verbindung zur Datenbank erzeugen
        connection = sqlite3.connect("stand.db")

        # Datensatz-Cursor erzeugen
        cursor = connection.cursor()

        # Datenbanktabelle erzeugen
        sql = "CREATE TABLE spiel(" \
            "name TEXT, " \
            "zeit TEXT, " \
            "SpielName TEXT, " \
            "info TEXT)"
        cursor.execute(sql)

        # Verbindung beenden
        connection.close()
def create_user_db():
    if os.path.exists("user.db"):
        print("user.db bereits vorhanden")
        
    else:
        # Verbindung zur Datenbank erzeugen
        connection = sqlite3.connect("user.db")

        # Datensatz-Cursor erzeugen
        cursor = connection.cursor()

        # Datenbanktabelle erzeugen
        sql = "CREATE TABLE user(" \
            "uname TEXT, " \
            "info TEXT)"
        cursor.execute(sql)
        # Verbindung beenden
        connection.close()

creat_stand_db()
create_user_db()

