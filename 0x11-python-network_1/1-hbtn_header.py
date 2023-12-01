#!/usr/bin/python3
"""
It send request to get the request ID

"""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
