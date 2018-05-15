#!/usr/bin/env python2
#  -*- coding: utf-8 -*-
# First draft
__author__ = 'nighter@nighter.se'

import requests
import couchdb
import string
import random
import base64
import cPickle
import sys
import os
import re

from hashlib import md5

HOST = 'http://localhost:5000'

def submit(character='', quote=''):

    session = requests.Session()
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'zip, deflate',
               'Referer': 'http://localhost:5000/submit',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Content-Length': 'close',
               'Upgrade-Insecure-Requests': '1'}


    postData = "character=" + character + "&quote=" + quote
    r = session.post(HOST + '/submit', data=postData, headers=headers)
    #m = re.search(r'([A-Za-z0-9]{30,})', r.text[750:])
    print(r.text)

def check(character='', quote=''):

    p_id = md5(character + quote).hexdigest()
    session = requests.Session()
    postData = {"id": p_id}
    r = session.post(HOST + '/check', data=postData)
    print(r.text)



if __name__ == '__main__':

    submit('Homer', 'Hello')

