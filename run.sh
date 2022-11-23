#!/bin/sh

python -c "import qrcode"
if [ $? -eq 1 ]; then
	pip install qrcode
else
cat party.sql | sqlite3 party.db

export FLASK_APP=main.py

flask run
