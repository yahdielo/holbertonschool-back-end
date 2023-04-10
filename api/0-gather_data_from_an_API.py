#!/usr/bin/python3
import requests
import json
from sys import argv

if __name__ == "__main__":
    user_id = eval(argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(user_url)
    _response = requests.get(todo_url)
    todo_response = _response.json()
    user_response = response.json()
    count = 0
    task_completed = []

    # Getting user name
    for user in user_response:
        if user['id'] == user_id:
            user_name = user['name']
    print(user_name)
    #create list of users wit id and name

    for task in todo_response:
        if task['userId'] == user_id:
            if task['completed']:
                count += 1
                task_completed.append(task['title'])

    print(f'Employee {user_name} is done with tasks({count}/20):')
    for i in task_completed:
        print(f'\t {i}')




