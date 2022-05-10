import os, sys, sqlite3

if os.path.exists("stand.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

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
