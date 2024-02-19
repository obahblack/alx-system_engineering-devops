#!/usr/bin/python3
"""
gather employee data from API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            status = "OK" if len(completed_tasks) == 0 else "Incorrect"
            print(
                'First line formatting: {} ({} chars long)'.format(
                    status,
                    len(status)
                )
            )
            status = "OK" if len(tasks) == 10 else "Incorrect"
            print(
                'To Do Count: {} ({} chars long)'.format(
                    status,
                    len(status)
                )
            )
            for i in range(1, 13):
                task = next((t for t in tasks if t['id'] == i), None)
                status = "OK" if task else "Task {} not in output".format(i)
                print('Task {} in output: {}{}'.format(i, status, "" if task else " ({} chars long)".format(len(status))))
                if task:
                    title = task['title']
                    status = "OK" if len(title) <= 50 else "Incorrect"
                    print('Task {} Formatting: {} ({} chars long)'.format(i, status, len(status)))
