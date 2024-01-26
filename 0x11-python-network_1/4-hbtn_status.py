#!/usr/bin/python3
"""
 fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    content = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(content.text)}")
    print(f"\t- content: {content.text}")
