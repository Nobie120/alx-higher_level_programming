#!/usr/bin/python3
"""
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    content = requests.get(url)
    if content.status_code >= 400:
        print(f"Error code: {content.status_code}")
    else:
        print(content.text)
