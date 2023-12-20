#!/usr/bin/python3
"""
    gathers data from api
"""
import requests
from sys import argv

if __name__ == '__main__':
    """
        Main function.
    """

    url = 'https://jsonplaceholder.typicode.com/'
    #sets the api url

    id = argv[1]
    info = requests.get(url + f'users/{id}').json()
    tasks = requests.get(url + f'users/{id}/todos').json()
    #requests info from the api

    done_tasks = [task for task in tasks if task["completed"]]
    #creates a dict with the completed tasks

    print(f'Employee {info["name"]} is done with tasks', end=' ')
    print(f'({len(done_tasks)}/{len(tasks)}):')

    for task in done_tasks:
        print(f'\t ' + task["title"])
