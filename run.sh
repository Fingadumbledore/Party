#!/bin/sh
if [ ! -e party.db ]; then
    cat ./Config/party.sql | sqlite3 party.db
fi

if [ ! -e ./Config/log/server.log ]; then
    touch ./Config/log/server.log
fi

if [ ! -e ./Config/log/chat.log ]; then
    touch ./Config/log/chat.log
fi

export RUN_WITH_SH=1

export FLASK_APP=main.py


#if [ "$(id -u)" != "0" ]; then
#    echo "Dieses Skript muss mit sudo ausgeführt werden!"
#    exit 1
#fi

python3 main.py $@
