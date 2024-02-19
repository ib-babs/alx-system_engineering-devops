#!/usr/bin/python3
"""Python script to export data in the JSON format.
All employee data"""
import json
import requests
import sys

if __name__ == "__main__":
    # URLs
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos/"

    # Requests
    all_employee = requests.get(url=user_url)
    all_task = requests.get(url=todo_url)

    # JSON
    all_employee_json = all_employee.json()
    all_task_json = all_task.json()

    with open('todo_all_employees.json', 'w') as file_csv:

        ids = [id['id'] for id in all_employee_json]
        tasks = {}
        for id in ids:
            tasks[id] = []
        for task in all_task_json:
            for k, v in tasks.items():
                if k == task['userId']:
                    tasks[k].append({'username': all_employee_json[k-1][
                        'username'],
                        "task": task['title'],
                        "completed": task['completed']
                    })
        json.dump(tasks, file_csv)
