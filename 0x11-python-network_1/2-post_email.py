#!/usr/bin/python3
"""0-hbtn_status fetches https://alx-intranet.hbtn.io/status
and prints the body content
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))
