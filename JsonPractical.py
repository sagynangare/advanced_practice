GITHUB_API='https://api.github.com'

import requests
import getpass
import json
from urlparse import urljoin

def main():
    username = raw_input('Github Username: ')
    password = raw_input('Github password: ')
    note = raw_input('Note (optional): ')

    url = urljoin(GITHUB_API,'authorizations')
    payload = {}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth=(username, password),
        data = json.dumps(payload),
        )
    print(res.text)
if __name__=='__main__':
    main()
