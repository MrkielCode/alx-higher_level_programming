#!/bin/bash
#checking the size of the url

curl -s "$1" | wc -c 
