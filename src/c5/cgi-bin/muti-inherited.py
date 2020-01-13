# coding: UTF-8
# 多重継承を利用するクラス

class A:
    def print(self):
        print('A')

class AB:
    def print(self):
        print('AB')

class AC:
    def print(self):
        print('AC')

class D(A, AB, AC):
    pass

obj = D()
obj.print()
