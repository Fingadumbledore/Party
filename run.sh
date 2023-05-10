#!/bin/sh
cat ./Config/party.sql | sqlite3 party.db

export FLASK_APP=main.py

sudo python3 main.py $@
