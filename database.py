import os, sys, sqlite3

# Existenz feststellen
if os.path.exists("party.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("party.db")
cursor = connection.cursor()

sql = "CREATE TABLE user(" \
      "userID INTEGER UNIQUE PRIMARY KEY, " \
      "username TEXT, " \
      "sessionID INTEGER, " \
      "info TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE session(" \
      "sessionID INTEGER UNIQUE PRIMARY KEY, " \
      "sessionname TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE chat(" \
      "sessionID TEXT " \
      "userid TEXT " \
      "chatmessage TEXT, " \
      "Zeit TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE game(" \
      "sessionID TEXT " \
      "userID TEXT " \
      "Spielname TEXT, " \
      "Zeit TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE planer(" \
      "event TEXT " \
      "zeit TEXT " \
      "sessionID TEXT);"
cursor.execute(sql)


connection.close()