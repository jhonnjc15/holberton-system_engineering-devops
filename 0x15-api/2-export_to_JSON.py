#!/usr/bin/python3
"""Script that, using this REST API https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information
about his/her TODO list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    name = user.get("username")

    data = []
    for i in todos:
        data.append({
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": name})

    with open("{}.json".format(user_id), "w", encoding="utf-8") as json_file:
        json.dump({user_id: [i for i in data]}, json_file)
