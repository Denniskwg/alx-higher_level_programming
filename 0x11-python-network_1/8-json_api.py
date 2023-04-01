#!/usr/bin/python3
"""5-hbtn_status fetches a url using requests library
and prits a header value
"""


if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = sys.argv[1]
    except IndexError as e:
        payload = {'q': ""}
    else:
        payload = {'q': letter}
    r = requests.post(url, data=payload)
    try:
        rseponse = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
    else:
        if response == {}:
            print("No result")
        else:
            id = response.get('id')
            name = response.get('name')
            print("[{}] {}".format(id, name))
