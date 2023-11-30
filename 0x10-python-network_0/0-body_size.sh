#!/usr/bin/env bash
#checking the size of the url
url=$1
curl -s -o /dev/null -w "%{size_download}" "$url"
echo
