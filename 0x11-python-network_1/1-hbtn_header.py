#!/usr/bin/python3
"""0-hbtn_status fetches https://alx-intranet.hbtn.io/status
and prints the body content
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
