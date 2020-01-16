# coding: UTF-8
#  演算子のオーバーロードするプログラム

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Pos(10, 20)
p2 = Pos(30, 40)

p3 = p1 + p2
print(p3)
