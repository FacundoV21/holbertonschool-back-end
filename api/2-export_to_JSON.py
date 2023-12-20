#!/usr/bin/python3
"""
    gathers data from api
"""
import requests
from sys import argv
import json

if __name__ == '__main__':
    """
        Main function.
    """

    url = 'https://jsonplaceholder.typicode.com/'

    id = int(argv[1])
    info = requests.get(url + f'users/{id}').json()
    tasks = requests.get(url + f'users/{id}/todos').json()

    dictionary = []

    for task in tasks:
        baseDict = {'task': task["title"],
                    'completed': task["completed"],
                    'username': info["username"],
        }
        dictionary.append(baseDict)

    with open(f"{id}.json", 'w') as f:
        json.dump({id: dictionary}, f)
