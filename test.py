import pyqrcode
ip = "http://192.168.178.56:8000"
url = pyqrcode.create(ip)
print(url.terminal(quiet_zone=1))


