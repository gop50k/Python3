# coding: UTF-8
# アクセサ、ゲッターセッターを実装したプログラム

class Clock:
    def __init__(self, hour):
        self._hour = hour

    @property
    def hour(self):
        return self._hour

c = Clock(10)
print(c.hour)
