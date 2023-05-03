#!/bin/bash
# This script sends a GET request to the URL passed as the first argument and displays the body of the response
curl -s -L -X GET "$1"
