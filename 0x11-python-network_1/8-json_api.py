#!/usr/bin/python3
"""
This script sends a request with json as paramter
and returns json data
"""

from sys import argv
import requests

url = "http://0.0.0.0:5000/search_user"

if len(argv) == 2:
    q = argv[1]
    try:
        r = requests.get(url).json(q)
    except requests.exceptions.JSONDecodeError as e:
        print(" Not a valid JSON")
    else:
        print("No result")
else:
    q=""
    print("No result")
