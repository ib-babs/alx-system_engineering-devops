#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
from io import StringIO
import requests
import sys

if __name__ == "__main__":
    # URLs
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos/"

    # Url Parameters
    id = {'id': sys.argv[1]}
    completed_todo = {'userId': sys.argv[1], 'completed': 'true'}
    total_todo = {'userId': sys.argv[1]}

    # Requests
    employee = requests.get(url=user_url, params=id)
    all_task = requests.get(url=todo_url, params=total_todo)

    with open(f'{sys.argv[1]}.csv', 'w') as file_csv:

        csv_writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        all_task_json = all_task.json()
        employee_json = employee.json()[0]
        for task in all_task_json:
            selected_part = (
                task['userId'], employee_json['username'], task['completed'],
                task['title'])
            csv_writer.writerow(selected_part)
