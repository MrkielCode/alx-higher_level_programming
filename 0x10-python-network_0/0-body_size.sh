#!/bin/bash
# it takes a url and send a request to get the body size

curl -s "$1" | wc -c 
