#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
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
    finished_task = requests.get(url=todo_url, params=completed_todo)
    unfinished_task = requests.get(url=todo_url, params=total_todo)

    finished_task_json = finished_task.json()
    output = 'Employee {} is done with tasks({}/{}):'

    print(output.format(employee.json()[0].get('name'),
                        len(finished_task_json), len(unfinished_task.json())))
    for finish in finished_task_json:
        print(f"\t {finish.get('title')}")
