#!/usr/bin/python3
"""
displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    content = requests.get(url)
    print(content.headers.get("X-Request-Id"))
