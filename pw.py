#! /usr/bin/python3
# pw.py - Insecure password locker

import sys, pyperclip

PASSWORDS = {'email': 'abcd1234',
             'blog': 'shitty999',
             'luggage': '9999'}

if len(sys.argv) < 2:
    print('usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
        
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('there is no account named ' + account)
