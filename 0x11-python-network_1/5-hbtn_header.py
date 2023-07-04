#!/usr/bin/python3
""" a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header """

if __name__ == '__main__':
    import sys
    import requests
    try:
        resp = requests.get(sys.argv[1])
        print(resp.headers.get('X-Request-Id'))
    except Exception:
        pass
