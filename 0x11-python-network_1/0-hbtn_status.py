#!/usr/bin/python3
"""
sending a request and getting a status code

"""
from urllib.request import Request, urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.getcode()
    print(status)
