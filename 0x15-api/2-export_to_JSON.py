#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
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

    with open(f'{sys.argv[1]}.json', 'w') as file_csv:

        all_task_json = all_task.json()
        employee_json = employee.json()[0]
        output = {
            id['id']:  []}
        for task in all_task_json:
            output[id['id']].append({"task": task['title'],
                                     "completed": task['completed'], 'username': employee_json['username'],
                                     })
        json.dump(output, file_csv)
