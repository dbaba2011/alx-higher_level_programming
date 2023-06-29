#!/bin/bash
# A script that display all the http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
