#!/usr/bin/pythonr
import requests

data = requests.get('https://alx-intranet.hbtn.io/status')
print(data)