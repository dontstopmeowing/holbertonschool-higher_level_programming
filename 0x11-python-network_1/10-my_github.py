#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    usern = argv[1]
    token = argv[2]
    response = requests.get(url, auth=(usern, token))
    print("{}".format(response.json().get("id")))
