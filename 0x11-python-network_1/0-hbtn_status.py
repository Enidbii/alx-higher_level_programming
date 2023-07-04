#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        fetch_body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(fetch_body)))
        print('\t- content: {}'.format(fetch_body))
        print('\t- utf8 content: {}'.format(fetch_body.decode('utf-8')))
