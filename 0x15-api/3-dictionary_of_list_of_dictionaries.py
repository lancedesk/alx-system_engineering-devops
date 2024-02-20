#!/usr/bin/python3
"""
Returns information about given employee ID TODO list progress
Using this REST API
And exports data in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Export TODO list progress to JSON file
    """

    """
    Fetching user information
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_tasks = {}

    """
    Fetching user's TODO list
    """
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        tasks = response.json()

        all_tasks[user_id] = []
        for task in tasks:
            task_data = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            all_tasks[user_id].append(task_data)

    """
    Writing data to JSON file
    """
    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data exported to {filename}")
