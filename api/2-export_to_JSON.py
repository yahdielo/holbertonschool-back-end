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
    d_task = {}
    list_of_task = []
    full_dict = {}

    for user in user_response:
        if user['id'] == user_id:
            user_name = user['username']

    for task in todo_response:
        if task['userId'] == user_id:
            d_task = {'task': task['title'],
                      'completed': task['completed'],
                      'username': user_name}
            list_of_task.append(d_task)

    full_dict[user_id] = list_of_task

    with open(f'{user_id}.json', 'w') as f:

        json.dump(full_dict, f)
