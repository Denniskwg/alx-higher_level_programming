#!/usr/bin/python3
"""5-hbtn_status fetches a url using requests library
and prits a header value
"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
