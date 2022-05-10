from client import build_window
import os, sys
from pathlib import Path

if  os.path.exists("ip.txt"):
    print("Datei bereits vorhanden")
else:
    myfile = Path('ip.txt')
    myfile.touch(exist_ok=True)
    ip = input("Ihre LOKALE IP: ")
    ip = "http://" + ip + ":8000"

    datei = open('ip.txt','w')
    datei.write(ip)
    datei.close()
    
build_window()
