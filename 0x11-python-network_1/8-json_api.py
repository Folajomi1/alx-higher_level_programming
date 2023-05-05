#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
If the response body is properly JSON formatted and not empty, it displays the id and name in the format: [<id>] <name>.
Otherwise, it displays specific messages based on the JSON response.

Usage: ./8-json_api.py [letter]
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

