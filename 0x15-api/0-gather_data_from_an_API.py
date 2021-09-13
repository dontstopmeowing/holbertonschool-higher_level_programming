#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
from sys import argv


def response(userId):
    """This function contains all the data sent from the server."""
    if userId.isdigit():
        user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".
            format(userId))

        data = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(userId))

        if user.status_code == 200 and data.status_code == 200:
            return user.json(), data.json()
        else:
            print('An error has occurred.')
    else:
        return


def process(data):
    """This function processes all the data provided by the server."""
    completed = []
    total = 0
    user, data = response(data)
    for i in data:
        if i.get('completed') is True:
            total += 1
            completed.append(i.get('title'))

    print("Employee {:s} is done with tasks({:d}/{:d}):".
          format(user.get('name'), total, len(data)))

    for tasks in completed:
        print("\t {:s}".format(tasks))


if __name__ == "__main__":
    if argv[1].isdigit():
        process(argv[1])
    else:
        print("ye nice try")
