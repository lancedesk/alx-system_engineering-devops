#!/usr/bin/python3
"""
Returns information about given employee ID TODO list progress
Using this REST API
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
    user_id = int(argv[1])

    """
    Find the user by ID
    """
    for user in users.json():
        if user.get('id') == user_id:
            employee_name = user.get('username')
            break

    """
    Fetching user's TODO list
    """
    todos = requests.get(
            f"http://jsonplaceholder.typicode.com/todos?userId={user_id}"
            )

    """
    File name based on user ID
    """
    file_name = f"{user_id}.csv"

    """
    Writing data to CSV file
    """
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = [
                      'USER_ID',
                      'USERNAME',
                      'TASK_COMPLETED_STATUS',
                      'TASK_TITLE'
                     ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        """
        Write each todo item as a row in the CSV file
        """
        for todo in todos.json():
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': todo.get('completed'),
                'TASK_TITLE': todo.get('title')
            })

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    export_to_csv()
