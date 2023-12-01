#!/usr/bin/python3
"""
It send request to server and it returns the X-Request-Id
"""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
