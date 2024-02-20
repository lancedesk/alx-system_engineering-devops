#!/usr/bin/python3
"""
Returns information about given employee ID TODO list progress
Using this REST API
And exports data in JSON format
"""

import json
import requests
from sys import argv


def export_to_json():
    """
    Export TODO list progress to JSON file
    """

    """
    Fetching user information
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            username = user.get('username')
            break

    """
    Fetching user's TODO list
    """
    tasks = []
    todos = requests.get(
            f"http://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
            )
    for todo in todos.json():
        tasks.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })

    """
    Writing data to JSON file
    """
    filename = f"{argv[1]}.json"
    with open(filename, "w") as jsonfile:
        json.dump({argv[1]: tasks}, jsonfile)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    export_to_json()
