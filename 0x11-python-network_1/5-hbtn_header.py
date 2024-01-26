#!/usr/bin/python3
"""
displays the value of the variable
X-Request-Id in the response header
"""
import requests, sys


if __name__ == "__main__":
    content = requests.get(sys.argv[1])
    print(content.headers.get("X-Request-Id"))
