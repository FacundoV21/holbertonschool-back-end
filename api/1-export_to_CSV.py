#!/usr/bin/python3
"""
    gathers data from api
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    """
        Main function.
    """

    url = 'https://jsonplaceholder.typicode.com/'

    id = argv[1]
    info = requests.get(url + f'users/{id}').json()
    tasks = requests.get(url + f'users/{id}/todos').json()

    with open(f'{id}.csv', 'w', newline='') as f:

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([id, info['name'], task['completed'],
                            task['title']],)
