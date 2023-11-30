#!/bin/bash
# script that sends a POST request using json
curl -s -H "Content-Type: application/json" "$1" -d @"$2"
