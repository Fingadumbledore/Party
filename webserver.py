from http.server import HTTPServer, BaseHTTPRequestHandler
from argparse import ArgumentParser
import http.server
import socketserver
import time
import logging
import os, sys, sqlite3
from urllib import parse
import json
import requests
import shutil

PORT = 8000
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date
sessionID = "/S1"
dbstatus = "Null"
sessionConfig = "F"
name = "f"
 
def create_DB():
        if os.path.exists("party.db"):
            print("Datei bereits vorhanden")
            sys.exit(0)

        # Verbindung zur Datenbank erzeugen
        connection = sqlite3.connect("party.db")

        # Datensatz-Cursor erzeugen
        cursor = connection.cursor()

        # Erzeuge Tabelle Spiel
        sql = "CREATE TABLE spiel(" \
            "username TEXT, " \
            "Spiel TEXT, " \
            "Zeit TEXT, " \
            "info TEXT)"
        cursor.execute(sql)
         # Erzeuge Tabelle Session
        sql = "CREATE TABLE session(" \
            "Sessionname TEXT, " \
            "Spieler TEXT, " \
            "Datum TEXT, " \
            "info TEXT)"
        cursor.execute(sql)
        

class Serve(BaseHTTPRequestHandler):

    def led_controll():
        print("in development")

    def restore_session(sessionConfig):
        print("Restoring Session")

  
       


    def log_server(self, log):
        datei = open('server.log','a')
        datei.write('\n' + " " + log )
        log = date
        datei.close()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/signin':
            self.path == '/create_user.html'
        if self.path == '/login':
            self.path == '/login.html'
        if self.path == sessionID:
            self.path == '/session.html'
        
        

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            log = date + " 200"
            # datei.write('\n' + " " + date)
        except:
            file_to_open = "File not found"
            self.send_response(400)
            log = date + " " +file_to_open
        finally:
            
            self.log_server(log)
          

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

        parsed = parse.urlparse(self.path)

    def do_POST(self):

        try:
            self.send_responses(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile(bytes('{"time": "' + date + '"}',"utf-8"))
        except:
                self.send_response(400)
                #print("POST error")
   
def main(name):   
    ordner = '/' + name     
    create_DB()   
   
    try:
         httpd = HTTPServer(('0.0.0.0', PORT), Serve)
         #log = log + "server is now running on" + str(PORT)
         print("server is now running on http://127.0.0.1:" + str(PORT))
         httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")
    shutil.move('party.db', name)
    shutil.move(name, 'sammlung')

