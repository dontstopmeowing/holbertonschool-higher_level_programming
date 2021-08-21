#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    request = requests.post(url, data={"q": q})
    try:
        response = request.json()
        if len(response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except Exception:
        print("Not a valid JSON")
