#!/usr/bin/python3
"""5-hbtn_status fetches a url using requests library
and prits a header value
"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
