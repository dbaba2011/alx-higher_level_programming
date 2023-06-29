#!/bin/bash
# a bash script that sends a json post request and display the response of the b#ody
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
