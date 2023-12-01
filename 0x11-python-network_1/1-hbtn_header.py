#!/usr/bin/python3
"""
It send request to get the request ID

"""
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
