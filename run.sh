
python -c "import qrcode"
if [ $? -eq 1 ]; then
	pip install qrcode
else
	echo "qrcode package is installed"
fi
cat party.sql | sqlite3 party.db

export FLASK_APP=main.py


 flask run
