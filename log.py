import os
import re
import time

date = lambda: time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log_dir = "./Config/log/"
old_logs_dir = "./Config/log/old/"

def clear_log():
    chat_files = []
    server_files = []
    for filename in os.listdir(log_dir):
        if re.match(r"^chat\d+\.log$", filename):
            chat_files.append(filename)
        elif re.match(r"^server\d+\.log$", filename):
            server_files.append(filename)

    chat_files.sort(key=lambda x: int(re.search(r"\d+", x).group()))
    server_files.sort(key=lambda x: int(re.search(r"\d+", x).group()))

    if len(chat_files) >= 10:
        for filename in chat_files[:-1]:
            with open(os.path.join(log_dir, filename), "r") as log_file:
                log_data = log_file.readlines()
            log_data = combine_duplicate_lines(log_data)
            if log_data:
                move_to_old_logs(filename, log_data)
            os.remove(os.path.join(log_dir, filename))
    if len(server_files) >= 10:
        for filename in server_files[:-1]:
            with open(os.path.join(log_dir, filename), "r") as log_file:
                log_data = log_file.readlines()
            log_data = combine_duplicate_lines(log_data)
            if log_data:
                move_to_old_logs(filename, log_data)
            os.remove(os.path.join(log_dir, filename))

def combine_duplicate_lines(log_data):
    combined_lines = []
    current_line = None
    for line in log_data:
        if "[INFO] )called /get with GET" in line:
            timestamp = re.search(r"(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})", line).group(1)
            if current_line:
                current_line = current_line[:19] + " - " + timestamp + current_line[19:]
                combined_lines.append(current_line)
            current_line = timestamp + line[19:]
        else:
            if current_line:
                combined_lines.append(current_line)
            combined_lines.append(line)
            current_line = None

    if current_line:
        combined_lines.append(current_line)

    return combined_lines

def move_to_old_logs(filename, log_data):
    os.makedirs(old_logs_dir, exist_ok=True)
    with open(os.path.join(old_logs_dir, filename), "a") as old_log_file:
        old_log_file.writelines(log_data)

def log_server(log, type):
    """ server log""" 
    raise Exception("Deprecated, use insert_log()")

def chat_log(data, log_type):
    """ chat log """

    raise Exception("Deprecated, use insert_log()")

def insert_log(file: str, data: str, log_type: str):
    current_date = date()
    data = f"{current_date} [{log_type}] {data}\n"

    while True:
        full_file_name = os.path.join(log_dir, f"{file}.log")
        if os.path.exists(full_file_name):
            file_size = os.path.getsize(full_file_name)
            if file_size >= 1024 * 128:  # Überprüfe, ob die Dateigröße 1 MB überschreitet
                file = increment_filename(file)
            else:
                with open(full_file_name, "a") as log_file:
                    log_file.write(data)
                break
        else:
            with open(full_file_name, "w") as log_file:
                log_file.write(data)
            break

def increment_filename(file: str) -> str:
    match = re.match(r"^(.+?)(\d+)?$", file)
    if match:
        base_name = match.group(1)
        index = int(match.group(2)) + 1 if match.group(2) else 1
        return f"{base_name}{index}"
    else:
        return file + "1"

if __name__ == "__main__":
    print("Use main.py to use program")
