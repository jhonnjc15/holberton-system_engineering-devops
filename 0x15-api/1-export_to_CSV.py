#!/usr/bin/python3
"""Script that, using this REST API https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information
about his/her TODO list progress"""
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow(

                    [user_id, name, i.get("completed"), i.get("title")]
            )
