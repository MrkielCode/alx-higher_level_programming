#!/bin/bash
# it takes a url and send a request to get the body size
curl -s -o /dev/null -w "%{size_download}" "$1"; echo
