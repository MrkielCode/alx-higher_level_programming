#!/usr/bin/python3
"""
This scripts sends a request and return the X-REQUEST_ID

"""

import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(argv[1]).headers.get('X-Request-Id')
    print(response)
