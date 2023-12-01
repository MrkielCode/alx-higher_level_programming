#!/usr/bin/python3

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":

    email = urlencode({'email': argv[2]})
    url = argv[1]

    with urlopen(url, data=email.encode('ascii')) as response:
        data = response.read().decode('utf-8')
        print(data)
