# coding: UTF-8
# 発送料を計算するプログラム

import math

class CalcFee:
    def __init__(self):
        ''' 初期化メソッド '''
        self.shippinfee = 1000
        self.tax = 0.1
        self.value = 0

    def addItem(self, price):
        ''' 追加商品を加算するメソッド '''
        self.value += price

    def calc(self):
        ''' 最終的な料金を計算する '''
        total = self.value + self.shippinfee
        tax = math.ceil(total * self.tax)
        v = math.ceil(total + tax)
        return v

fee1 = CalcFee()
fee1.addItem(500)
print(fee1.calc(), "円")

fee2 = CalcFee()
fee2.shippinfee = 1500
fee2.addItem(500)
fee2.addItem(800)
fee2.addItem(1000)
print(fee2.calc(), "円")
