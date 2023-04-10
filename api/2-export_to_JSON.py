#!/usr/bin/python3
""" making api requests to get specific data"""

import csv
import requests
from sys import argv
import json

if __name__ == "__main__":
    user_id = eval(argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(user_url)
    _response = requests.get(todo_url)
    todo_response = _response.json()
    user_response = response.json()
    dict_of_task = []
    full_dict = {}

    for user in user_response:
        if user['id'] == user_id:
            user_name = user['username']

    for task in todo_response:
        if task['userId'] == user_id:
            full_dict = {'task': task['title'],
                         'completed': task['completed'],
                         'username': user_name}
            dict_of_task.append(full_dict)

    with open(f'{user_id}.json', 'w') as f:

        json.dump(dict_of_task, f)
