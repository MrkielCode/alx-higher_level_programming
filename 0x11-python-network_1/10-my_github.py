#!/usr/bin/python3
"""
This script uses github API and to Auth Users
"""
import requests
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]

    # getting a the user details
    api_url = 'https://api.github.com/user'
    user = (username, password)
    header = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
        }
    response = requests.get(api_url, auth=user, headers=header)

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")
