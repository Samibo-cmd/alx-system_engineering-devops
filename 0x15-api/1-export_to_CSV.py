#!/usr/bin/python3
"""A script that fetches info about a given employee using an api
   and exports it in csv format"""

import sys
import requests
import json


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # gets user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    # gets info from api
    response = requests.get(user_url)
    # pulls data from api
    data = response.text
    # parses the data into JSON format
    data = json.loads(data)
    # extracts user data, in this case, username of employee
    user_name = data[0].get('username')
    # print("id is: {}".format(user_id))
    # print("name is: {}".format(user_name))

    # gets user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    # gets info from api
    response = requests.get(tasks_url)
    # pulls data from api
    tasks = response.text
    # parses the data into JSON format
    tasks = json.loads(tasks)

    # builds the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
