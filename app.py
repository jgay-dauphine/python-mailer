#!/usr/bin/env python3

from gmail import Gmailer
from email.mime.text import MIMEText

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print('Read Configuration:')
print('~~', config['DEFAULT']['gmail_user'])
print('~~', config['DEFAULT']['gmail_password'])

x = Gmailer(config['DEFAULT']['gmail_user'], config['DEFAULT']['gmail_password'])

body = MIMEText('Coucou')

x.send_mail(body)