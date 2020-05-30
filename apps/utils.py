import datetime
import json

def current_time():
    now = datetime.datetime.now()
    current_time = datetime.datetime.strftime(now, '%d %B %Y %X')
    return current_time


def create_json(data, name):
    with open(f"corona flask api/data/{name}.json", "w") as write_file:
        json.dump(data, write_file)


def read_json(file_name):
    with open(f"corona flask api/data/{file_name}.json", "r") as read_file:
        return json.load(read_file)
