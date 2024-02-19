#!/usr/bin/python3
"""
Python script that, using a given REST API, retrieves information about an employee's TODO list progress.
"""

import sys
import requests

# Changed the docstring to clarify the purpose of the script.

def get_todo_list(employee_id):
    """
    Retrieve the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # API endpoint to retrieve user information
    user_url = f"{base_url}/users/{employee_id}"

    # API endpoint to retrieve user's TODO list
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Retrieve user information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Retrieve user's TODO list
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        # Extract user information
        employee_name = user_data.get('name')
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task.get('completed'))

        # Adjusted the print statement to include parentheses around the completed tasks count.
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Changed the indentation of the print statement and added a colon to match the example output format.
        for task in todo_data:
            if task.get('completed'):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list(employee_id)
