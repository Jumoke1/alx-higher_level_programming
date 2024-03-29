#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the value"""
import sys
import urllib.request


if __name__ == "__main__":
     with urllib.request.urlopen(argv[1]) as response:
        html_content  = response.read()
        headers = response.getheader('X-Request-Id')
    print(headers)
