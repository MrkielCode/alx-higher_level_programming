#!/usr/bin/python3

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    link = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(link, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)