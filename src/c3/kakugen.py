# coding: UTF-8
# ランダムに格言を表示するプログラム

import random

kakugen = [
    "能ある鷹は爪隠す",
    "豚に真珠",
    "二度あることは三度ある",
    "立てば芍薬座れば牡丹歩く姿は百合の花"
]

i = random.randint(0, len(kakugen)-1)

print(kakugen[i])
