#!/usr/bin/python3
""" akes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8). """


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            url_respond = response.read()
            print(url_respond.decode('utf-8'))

    except urllib.error.HTTPError as p_error:
        print("Error code: {}".format(p_error.code))
