#!/usr/bin/python3
"""0-hbtn_status fetches https://alx-intranet.hbtn.io/status
and prints the body content
"""


if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        response = response.read()
        print("Body response:")
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("    - utf8 content: {}".format(response.decode('utf-8')))
