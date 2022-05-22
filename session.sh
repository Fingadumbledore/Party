#!/bin/bash
d=`date +%Y-%m-%d-%H-%M` 

mkdir $d
python3 database.py
cp database.py $d
mv session.png $d
mv stand.db $d
mv user.db $d
cp index.html $d
#echo  $d >> verlauf.txt
cd $d
mkdir user_image
mkdir game_image
touch config.txt

exit -1