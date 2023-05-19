""" Server logging system """
import os
import time


date = lambda: time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))

def clear_log():
    """ clearing log """
    print("f")

def log_server(log, type):
    """ server log""" 
    raise Exception("Deprecated, use insert_log()")
    file_size = os.path.getsize('./Config/log/server.log')
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    log = date + ' [' + type + '] ' + log
    datei = open('./Config/log/server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()
        

def chat_log(data, log_type):
    """ chat log """

    raise Exception("Deprecated, use insert_log()")
    file_size = os.path.getsize('./Config/log/chat.log')
    date = lambda: time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
    if file_size >= 1024*1024:
        clear_log()
    current_date = date()
    data = f'{current_date} [{log_type}]  {data}\n'
    datei = open('./Config/log/chat.log', 'a')
    datei.write(data)
    data = date()
    datei.close()

def insert_log(file: str, data: str, log_type: str):
    full_file_name = f'./Config/log/{file}.log'
    file_size = os.path.getsize(full_file_name)
    if file_size >= 1024*1024:
        clear_log()
    current_date = date()
    data = f'{current_date} [{log_type}]  {data}\n'
    datei = open(full_file_name, 'a')
    datei.write(data)
    data = date()
    datei.close()

if __name__ == "__main__":
    print("Use main.py to use program")
