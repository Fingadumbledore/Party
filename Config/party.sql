PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS user (
userID INTEGER PRIMARY KEY,
username TEXT,
sessionID INTEGER NOT NULL,
info TEXT
);

CREATE TABLE IF NOT EXISTS session (
sessionID INTEGER PRIMARY KEY,
sessionname TEXT,
sessionstatus TEXT,
sessiontyp TEXT,
sessionstartzeit TEXT
);

CREATE TABLE IF NOT EXISTS game (
sessionID INTEGER,
userID INTEGER,
spielname TEXT,
spielaktivität TEXT,
zeit TEXT,
PRIMARY KEY(sessionID, userID)
);

CREATE TABLE IF NOT EXISTS pointgame (
sessionID INTEGER,
userID INTEGER,
spielname TEXT,
spielaktivität TEXT,
punkte INTEGER,
PRIMARY KEY(sessionID, userID, spielname)
);

CREATE TABLE IF NOT EXISTS uploadgame (
sessionID INTEGER,
userID INTEGER,
spielname TEXT,
spielstand TEXT,
PRIMARY KEY(sessionID, userID, spielname)
);

CREATE TABLE IF NOT EXISTS planer (
eventid INTEGER PRIMARY KEY NOT NULL,
eventname TEXT,
eventzeit TEXT,
sessionID INTEGER,
eventstatus TEXT
);

CREATE TABLE IF NOT EXISTS mate (
mateid INTEGER PRIMARY KEY NOT NULL,
matename TEXT,
mateanzahl INTEGER
);

CREATE TABLE IF NOT EXISTS mws (
matekisten INTEGER,
sessionID INTEGER NOT NULL,
PRIMARY KEY(sessionID)
);

CREATE TABLE IF NOT EXISTS spiel (
spielname TEXT,
genre TEXT,
erscheinungsjahr TEXT,
gruppe TEXT,
teil INTEGER,
sessionID INTEGER NOT NULL,
bildname TEXT,
PRIMARY KEY(spielname, sessionID)
);

CREATE TABLE IF NOT EXISTS dateien (
dateiID INTEGER PRIMARY KEY NOT NULL,
dateiname TEXT,
sessionID INTEGER
);

CREATE TABLE IF NOT EXISTS musikMetaDaten (
  songID INTEGER PRIMARY KEY NOT NULL,
  artist TEXT,
  band TEXT,
  album TEXT,
  title TEXT,
  track TEXT,
  genre TEXT,
  composer TEXT,
  copyright TEXT,
  comment TEXT,
  releasedate TEXT,
  mp3_url TEXT,
  sessionID INTEGER,
  bildname TEXT
);


CREATE TABLE IF NOT EXISTS queue (
songID INTEGER,
sessionID INTEGER,
PRIMARY KEY(songID, sessionID)
);

CREATE TABLE IF NOT EXISTS messages (
messageID TEXT,
sessionID INTEGER,
username TEXT,
message TEXT,
timestamp TEXT,
PRIMARY KEY(messageID, sessionID)
);