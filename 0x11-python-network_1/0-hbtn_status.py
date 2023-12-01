#!/usr/bin/python3
"""
sending a request and getting a status code

"""
from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
    print("\t- utf8 content: {}".format(status.decode('utf8')))
