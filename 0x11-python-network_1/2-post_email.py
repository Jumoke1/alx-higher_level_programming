#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    my_value = {"email": sys.argv[2]}
    my_data = urllib.parse.urlencode(my_value).encode("ascii")

    my_request = urllib.request.Request(url, my_data)
    with urllib.request.urlopen(my_request) as response:
        print(response.read().decode("utf-8"))
