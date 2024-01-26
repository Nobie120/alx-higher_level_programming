#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request


    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        content = res.read()
        print("Body response:")
        print(f"\ttype: {type(content)}")
        print(f"\tcontent: {content}")
        print(f"\tutf8 content: {content.decode('utf-8')}")
