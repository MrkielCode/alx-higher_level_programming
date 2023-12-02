#!/usr/bin/python3
"""
This script sends a request with json as paramter
and returns json data
"""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
