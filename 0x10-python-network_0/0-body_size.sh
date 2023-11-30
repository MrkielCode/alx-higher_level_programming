#!/bin/bash
#checking the size of the url

curl -s -w "%{size_download}" "$1"
echo
