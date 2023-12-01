#!/usr/bin/python3

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urlencode({'email': email}).encode('ascii')
    req = Request(url, data=data, method='POST')
    with urlopen(req) as response:
        page = response.read()