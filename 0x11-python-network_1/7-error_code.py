#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    if requests.get(url).status_code >= 400:
        print("Error code: {}".format(requests.get(url).status_code))
    else:
        print(requests.get(url).text)
