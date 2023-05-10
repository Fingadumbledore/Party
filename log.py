import os
import time

def clear_log():
    print("f")

def log_server(log, type):
    file_size = os.path.getsize('server.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size <= 1024*1024:
        log = date + ' [' + type + '] ' + log
        datei = open('server.log', 'a')
        datei.write('\n' + " " + log)
        log = date
        datei.close()
    else:
        clear_log()

def chat_log():
    print("chat_log")