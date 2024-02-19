#!/usr/bin/python3
"""
gather employee data from API
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    id = int(sys.argv[1])
    user_url = '{}/users/{}'.format(REST_API, id)
    todo_url = '{}/todos?userId={}'.format(REST_API, id)

    user_req = requests.get(user_url)
    if user_req.status_code != 200:
        print("Error fetching user data.")
        sys.exit(1)
    user_data = user_req.json()
    emp_name = user_data.get('name')

    todo_req = requests.get(todo_url)
    if todo_req.status_code != 200:
        print("Error fetching TODO data.")
        sys.exit(1)
    todo_data = todo_req.json()
    tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get('completed'))

    print('Employee {} is done with tasks({}/{}):'.format(emp_name, completed_tasks, tasks))
    if completed_tasks > 0:
        for task in todo_data:
            if task.get('completed'):
                print('\t{}'.format(task.get('title')))
