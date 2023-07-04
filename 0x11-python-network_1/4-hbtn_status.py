!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(resp.content.decode()))
    print('\t- content:', resp.content.decode())
