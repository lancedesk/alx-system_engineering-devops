#!/usr/bin/python3
"""
Returns information about given employee ID TODO list progress
Using this REST API
And exports data in CSV format
"""

import csv
import requests
from sys import argv


def export_to_csv():
    """
    Export TODO list progress to CSV file
    """

    """
    Fetching user information
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            username = (user.get('username'))
            break

    """
    Fetching user's TODO list
    """
    task_status = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            task_status.append((todo.get('completed'),
                                todo.get('title')))

    """
    Writing data to CSV file
    """
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["user_id", "username",
                      "task_status", "task_title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in task_status:
            writer.writerow({"user_id": argv[1], "username": username,
                             "task_status": task[0],
                             "task_title": task[1]})


if __name__ == "__main__":
    export_to_csv()
