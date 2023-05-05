#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))

