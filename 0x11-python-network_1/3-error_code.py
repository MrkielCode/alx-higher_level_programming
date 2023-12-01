#!/usr/bin/python3
"""
script sends a request and return error
if not found
"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        data = urllib.request.Request(url)
        with urllib.request.urlopen(data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
