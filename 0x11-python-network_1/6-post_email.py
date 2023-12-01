#!/usr/bin/python3
"""
This script sends a POST Requests containing an email
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    response = requests.post(url, data={'email': email})
    print(response.text)
