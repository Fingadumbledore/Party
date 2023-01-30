PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS user (userID INTEGER PRIMARY KEY,username TEXT, sessionID INTEGER NOT NULL, info TEXT);
CREATE TABLE IF NOT EXISTS seession (sessionID INTEGER PRIMARY KEY, sessionname TEXT, sessionstatus TEXT, seessiontyp TEXT, sessionstartzei TEXT);
CREATE TABLE IF NOT EXISTS chat (sessionID INTEGER, userID INTEGER, chatmessage TEXT, ZEIT TEXT);
CREATE TABLE IF NOT EXISTS game (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, ZEIT TEXT);
CREATE TABLE IF NOT EXISTS pointgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielaktivität TEXT, Punkte INTEGER);
CREATE TABLE IF NOT EXISTS uploadgame (sessionID INTEGER, userID INTEGER, Spielname TEXT, Spielstand TEXT);
CREATE TABLE IF NOT EXISTS planer (eventid INTEGER PRIMARY KEY not NULL,eventname TEXT, eventzeit TEXT, sessionID INTEGER, eventstatus TEXT);
CREATE TABLE IF NOT EXISTS mate (matename TEXT, mateanzahl INTEGER, sessionID INTEGER);
CREATE TABLE IF NOT EXISTS mws (matekisten INTEGER, sessionID INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS spiel (spielname TEXT, Genre TEXT, Erscheinungsjahr TEXT, Gruppe TEXT, Teil INTEGER, sessionID INTEGER NOT NULL, Bildname TEXT);
CREATE TABLE IF NOT EXISTS dateien (dateiID INTEGER PRIMARY KEY NOT NULL, dateiname TEXT, sessionID INTEGER);
CREATE TABLE IF NOT EXISTS musikMetaDaten (songID INTEGER PRIMARY KEY Not NULL, artist TEXT, band TEXT, album TEXT, title TEXT, track TEXT, genre TEXT, composer TEXT, copyright TEXT, comment TEXT, releasedate TEXT, mp3_url TEXT, sessionID INTEGER, bildname TEXT);
CREATE TABLE IF NOT EXISTS queue (songID INTEGER, sessionID INTEGER)
CREATE TABLE IF NOT EXISTS messages (username TEXT, message TEXT, timestamp TEXT)
