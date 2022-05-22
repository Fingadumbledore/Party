#!/bin/bash
d=`date +%Y-%m-%d-%H-%M` 

mkdir -p past_sessions
mkdir $d
python3 database.py
cp database.py $d
mv session.png $d
mv stand.db $d
mv user.db $d
cp index.html $d
#echo  $d >> verlauf.txt
cd $d
mkdir $d/user_image
mkdir $d/game_image
touch $d/config.txt

exit -1