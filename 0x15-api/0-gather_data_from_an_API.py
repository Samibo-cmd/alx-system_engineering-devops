#!/usr/bin/python3
"""A script that fetches info about a given employee's ID using an api"""
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
    # extracts user data, in this case, name of employee
    name = data[0].get('name')
    # print("id is: {}".format(user_id))
    # print("name is: {}".format(name))

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

    # initializes completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    # initializes empty list for completed tasks
    completed_tasks = []
    # loops through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            # print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # prints the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
