#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
import urllib.parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    with urlopen(Request(argv[1], data)) as response:
        print(response.read().decode('utf-8'))
