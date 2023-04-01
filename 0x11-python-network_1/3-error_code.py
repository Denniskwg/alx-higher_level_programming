#!/usr/bin/python3
"""0-hbtn_status fetches https://alx-intranet.hbtn.io/status
and prints the body content
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    import urllib.error
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            response = response.read()
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        print(response.decode('utf-8'))
