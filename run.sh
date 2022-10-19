python3 database.py
export FLASK_APP=main.py
if [ -z $@ ]; then
  echo "please pass browser as argument, pass _, to get rid of this warning"
  exit 0
fi

sleep 3& $@ 127.0.0.1:5000& flask run