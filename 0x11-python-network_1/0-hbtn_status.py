#!/usr/bin/python3
"""0-hbtn_status fetches https://alx-intranet.hbtn.io/status
and prints the body content
"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(response)))
        print("\t - content: {}".format(response))
        print("\t - utf8 content: {}".format(response.decode('utf-8')))
