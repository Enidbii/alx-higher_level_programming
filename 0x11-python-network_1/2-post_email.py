#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    ema_il = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(ema_il)
    email = email.encode('ascii')
    url_request = urllib.request.Request(url, email)

    with urllib.request.urlopen(url_request) as response:
        url_respond = response.read()
    out = url_respond.decode('utf-8')
    print(out)
