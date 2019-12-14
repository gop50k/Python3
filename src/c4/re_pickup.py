# coding: UTF-8
# 正規表現を試すプログラム
import re

words = [
         'orange', 'october', 'octups',
         'order', 'banana', 'baby', 'busy'
]

pattern = r'oc.*'
print('ocで始まるパターン', pattern)
for word in words:
    if re.match(pattern, word):
        print('-', word)

pattern = r'b.*y'
print('bで始まりyで終わるパターン', pattern)
for word in words:
    if re.match(pattern, word):
        print('-', word)
