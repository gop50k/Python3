#!/usr/bin/env python3
# クッキーで訪問回数をカウントするプログラム

import os
import cgi
from http import cookies
import datetime

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
cnt = 1
if 'counter' in cookie:
    cnt = int(cookie['counter'].value + 1)

cookie['counter'] = cnt
expires = datetime.datetime.now() + datetime.timedelta(days=90)
cookie['counter']['expires'] = expires.strftime('%a, %d-%b-%y')

print('Content-Type: text/html; charset=utf-8')
print(cookie.output())
print('')
print('訪問回数=', cnt)
