import os, sys, sqlite3

# Existenz feststellen
if os.path.exists("party.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("party.db")
cursor = connection.cursor()

sql = "CREATE TABLE user(" \
      "userID INTEGER NOT NULL UNIQUE PRIMARY KEY, " \
      "username TEXT, " \
      "sessionID INTEGER, " \
      "info TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE session(" \
      "sessionID INTEGER NOT NULL UNIQUE PRIMARY KEY, " \
      "sessionname TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE chat(" \
      "sessionID INTEGER " \
      "userID INTEGER " \
      "Chatmessage TEXT, " \
      "Zeit TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE game(" \
      "sessionID INTEGER " \
      "userID INTEGER " \
      "Spielname TEXT, " \
      "Zeit TEXT);"
cursor.execute(sql)

sql = "CREATE TABLE planer(" \
      "event TEXT " \
      "zeit INTEGER " \
      "sessionID INTEGER);"
cursor.execute(sql)


connection.close()