#!/usr/bin/python3
"""4-hbtn_status fetches https://alx-intranet.hbtn.io/status
using requests library
"""


if __name__ == "__main__":
    import requests
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))
