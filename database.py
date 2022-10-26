import os, sys, sqlite3

def log_server(log):
    log = date + log
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()

def error_log(error):
    error = date + " [ERROR]"+ error
    datei = open('server.log', 'a')
    datei.write('\n' + " " + error)
    log = date
    datei.close()  

def problem_log(problem):
    problem = date + " [PROBLEM]"+ problem
    datei = open('server.log', 'a')
    datei.write('\n' + " " + problem)
    log = date
    datei.close() 

def warning_log(warning):
    warning = date + " [WARNING]"+ warning
    datei = open('server.log', 'a')
    datei.write('\n' + " " + warning)
    log = date
    datei.close()  


      # Existenz feststellen
if os.path.exists("party.db"):
      print("Datei bereits vorhanden")
      sys.exit(0)
      warning_log("Datenbank besteht bereits")

      # Verbindung zur Datenbank erzeugen
      connection = sqlite3.connect("party.db")
      warning_log("Verbindung mit Db wurde aufgenommen")
      cursor = connection.cursor()

      sql = "CREATE TABLE user(" \
            "userID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT," \
            "username TEXT, " \
            "sessionID INTEGER, " \
            "info TEXT);"
      cursor.execute(sql)
      log_server("user tabelle erstellt")

      sql = "CREATE TABLE session(" \
            "sessionID INTEGER UNIQUE PRIMARY KEY, " \
            "sessionname TEXT);"
      cursor.execute(sql)
      log_server("session tabelle erstellt")

      sql = "CREATE TABLE chat(" \
            "sessionID TEXT " \
            "userid TEXT " \
            "chatmessage TEXT, " \
            "Zeit TEXT);"
      cursor.execute(sql)
      log_server("chat tabelle erstellt")

      sql = "CREATE TABLE game(" \
            "sessionID TEXT " \
            "userID TEXT " \
            "Spielname TEXT, " \
            "Zeit TEXT);"
      cursor.execute(sql)
      log_server("game tabelle erstellt")

      sql = "CREATE TABLE planer(" \
            "event TEXT " \
            "zeit TEXT " \
            "sessionID TEXT);"
      cursor.execute(sql)
      log_server("planer tabelle erstellt")

      connection.close()
      log_server("Datenbank wurde erstellt")