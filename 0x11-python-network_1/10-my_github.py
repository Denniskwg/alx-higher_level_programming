#!/usr/bin/python3
"""10-my_github fetches a user id from github api using requests library
and prits the id
"""


if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/user"
    name = sys.argv[1]
    pwd = sys.argv[2]
    payload = {'name': name, 'Authorization': "Bearer {}".format(pwd)}
    r = requests.get(url, headers=payload)
    response = r.json()
    print(response.get('id'))
