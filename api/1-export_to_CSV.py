#!/usr/bin/python3
""" making api requests to get specific data"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = eval(argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(user_url)
    _response = requests.get(todo_url)
    todo_response = _response.json()
    user_response = response.json()
    task_completed = []
    row = []

    for user in user_response:
        if user['id'] == user_id:
            user_name = user['username']

    for task in todo_response:
        if task['userId'] == user_id:

            rows = [user_id, user_name, task['completed'], task['title']]
            row.append(rows)

    with open(f'{user_id}.csv', 'w') as f:

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row)
