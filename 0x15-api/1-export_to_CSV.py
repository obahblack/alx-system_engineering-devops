#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""

import csv
import requests
from sys import argv

def to_csv():
    """
    Retrieve data from the API and export it to a CSV file.
    """
    # Retrieve user information
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    
    # Find the username corresponding to the provided user ID
    for user in users.json():
        if user.get('id') == int(argv[1]):
            username = user.get('username')
            break
    
    # Collect task completion status and title for the given user ID
    task_status_title = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            task_status_title.append((todo.get('completed'), todo.get('title')))
    
    # Export data to CSV
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for task in task_status_title:
            writer.writerow({"USER_ID": argv[1], "USERNAME": username,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})

if __name__ == "__main__":
    to_csv()
