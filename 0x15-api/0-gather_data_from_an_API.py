#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress
using the provided REST API.
"""

import requests
import sys


def main():
    """
    Main function to retrieve and display TODO list progress for a given employee.
    """

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
        """
        Fetch user data
        """
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        """
        Fetch TODO list data
        """
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()
    except requests.exceptions.HTTPError as err:
        """
        Handle HTTP errors
        """
        print(f"Error fetching data: {err}")
        sys.exit(1)

    """
    Extracting user information
    """
    employee_name = user_data.get('name')

    """
    Calculating TODO list progress
    """
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    """
    Displaying TODO list progress
    """
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    main()

