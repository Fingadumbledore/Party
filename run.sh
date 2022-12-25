#!/bin/sh
if [ $? -eq 1 ]; then
	pip install qrcode
fi

cat party.sql | sqlite3 party.db

export FLASK_APP=main.py

flask run
