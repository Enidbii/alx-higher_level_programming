#!/usr/bin/python3
""" letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """


f __name__ == '__main__':
    import sys
    import requests

    """ requested data """
    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = ''
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': data})

    try:
        resp = response.json()
        if resp:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
