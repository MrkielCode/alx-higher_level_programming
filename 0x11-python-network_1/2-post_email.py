#!/usr/bin/python3

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    url = argv[1]

    req = Request(url, email)
    with urlopen(req) as response:
        data = response.read()
        print(data)
       
