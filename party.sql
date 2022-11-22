PRAGMA foreign_keys=ON;
CREATE TABLE user (userID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,username TEXT, sessionID INTEGER, info TEXT);
CREATE TABLE seession (sessionID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, sessionname TEXT, sessionstatus TEXT, seessiontyp TEXT);
CREATE TABLE chat (sessionID INTEGER, userID INTEGER, chatmessage TEXT, ZEIT TEXT);
CREATE TABLE game (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, ZEIT TEXT);
CREATE TABLE uploadgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielstand TEXT);
CREATE TABLE planer (eventname TEXT, eventzeit TEXT, sessionID INTEGER);
CREATE TABLE mate (matename TEXT, mateanzahl INTEGER, sessionID INTEGER);