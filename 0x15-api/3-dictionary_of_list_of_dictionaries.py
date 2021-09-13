#!/usr/bin/python3
"""Script that, using this REST API https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information
about his/her TODO list progress"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_data = {}
    for u in users:
        user_id = u.get('id')
        all_data[user_id] = []
        for t in requests.get(url + "todos",
                              params={"userId": user_id}).json():
            task = {'username': u.get('username'),
                    'task': t.get('title'),
                    'completed': t.get('completed')}
            all_data[user_id].append(task)

    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file)
