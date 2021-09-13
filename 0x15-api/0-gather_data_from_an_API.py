#!/usr/bin/python3
"""Script that, using this REST API https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information
about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    for i in todos:
        if i.get("completed") is True:
            completed.append(i.get("title"))
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get("name"), len(completed), len(todos)))
    for t in completed:
        print('\t {}'.format(t))
