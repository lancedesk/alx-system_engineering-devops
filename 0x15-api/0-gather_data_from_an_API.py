#!/usr/bin/python3
"""
Returns information about given employee ID TODO list progress
Using this REST API
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    """
    Fetching data from the REST API
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_response.raise_for_status()
        todo_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data: {err}")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    """
    Extracting user information
    """
    employee_name = user_data['name']

    """
    Calculating TODO list progress
    """
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    """
    Displaying TODO list progress
    """
    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_tasks}/{total_tasks}):"
    )
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")
