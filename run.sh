#!/bin/sh
if [ ! -e party.db ]; then
    cat ./Config/party.sql | sqlite3 party.db
fi

export FLASK_APP=main.py

if [ "$(id -u)" != "0" ]; then
    echo "Dieses Skript muss mit sudo ausgeführt werden!"
    exit 1
fi
touch chat.log
python3 main.py $@