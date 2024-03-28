#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import requests
import sys

def main():
    # Check if both URL and email are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request with email as parameter
    payload = {'email': email}
    response = requests.post(url, data=payload)

    # Display body of the response
    print(response.text)

if __name__ == "__main__":
    main()
