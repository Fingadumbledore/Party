#!/bin/sh

python -c "import qrcode"
if [ $? -eq 1 ]; then
	pip install qrcode
fi

md5sum -c .sums
if [ $? -eq 1 ]; then
	rm party.db
	cat party.sql | sqlite3 party.db
fi

export FLASK_APP=main.py

flask run
