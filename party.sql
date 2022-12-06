PRAGMA foreign_keys=ON;
CREATE TABLE user (userID INTEGER PRIMARY KEY,username TEXT, sessionID INTEGER NOT NULL, info TEXT);
CREATE TABLE seession (sessionID INTEGER PRIMARY KEY, sessionname TEXT, sessionstatus TEXT, seessiontyp TEXT);
CREATE TABLE chat (sessionID INTEGER, userID INTEGER, chatmessage TEXT, ZEIT TEXT);
CREATE TABLE game (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, ZEIT TEXT);
CREATE TABLE uploadgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielstand TEXT);
CREATE TABLE planer (eventname TEXT, eventzeit TEXT, sessionID INTEGER, eventstatus TEXT);
CREATE TABLE mate (matename TEXT, mateanzahl INTEGER, sessionID INTEGER);