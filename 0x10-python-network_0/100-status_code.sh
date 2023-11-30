#!/bin/bash
# print the status of request
curl -s -o /dev/null -w "%{http_code}" "$1"
