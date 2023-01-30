PRAGMA foreign_keys=ON;
CREATE TABLE user (userID INTEGER PRIMARY KEY,username TEXT, sessionID INTEGER NOT NULL, info TEXT);
CREATE TABLE seession (sessionID INTEGER PRIMARY KEY, sessionname TEXT, sessionstatus TEXT, seessiontyp TEXT, sessionstartzei TEXT);
CREATE TABLE chat (sessionID INTEGER, userID INTEGER, chatmessage TEXT, ZEIT TEXT);
CREATE TABLE game (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, ZEIT TEXT);
CREATE TABLE pointgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, Punkte INTEGER);
CREATE TABLE uploadgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielstand TEXT);
CREATE TABLE planer (eventid INTEGER PRIMARY KEY not NULL,eventname TEXT, eventzeit TEXT, sessionID INTEGER, eventstatus TEXT);
CREATE TABLE mate (matename TEXT, mateanzahl INTEGER, sessionID INTEGER);
CREATE TABLE mws (matekisten INTEGER, sessionID INTEGER NOT NULL);
CREATE TABLE spiel (spielname TEXT, Genre TEXT, Erscheinungsjahr TEXT, Gruppe TEXT, Teil INTEGER, sessionID INTEGER NOT NULL, Bildname TEXT);
CREATE TABLE dateien (dateiID INTEGER PRIMARY KEY NOT NULL, dateiname TEXT, sessionID INTEGER);
CREATE TABLE musikMetaDaten (songID INTEGER PRIMARY KEY Not NULL, artist TEXT, band TEXT, album TEXT, title TEXT, track TEXT, genre TEXT, composer TEXT, copyright TEXT, comment TEXT, releasedate TEXT, mp3_url TEXT, sessionID INTEGER, bildname TEXT);
CREATE TABLE queue (songID INTEGER, sessionID INTEGER)
CREATE TABLE messages (username TEXT, message TEXT, timestamp TEXT)