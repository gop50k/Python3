# coding: UTF-8
# QRコードを生成するコード

import qrcode
img = qrcode.make('http://kujirahand.com/')
img.save('qrcode-test.png')
