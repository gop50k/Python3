# coding: UTF-8
# アクセサ、ゲッターセッターを実装したプログラム

class Clock:
    def __init__(self, hour):
        self._hour = hour
        self._ampm = 'am'

    @property
    def hour(self):
        return self._hour

    @property
    def ampm(self):
        return self._ampm

    @hour.setter
    def hour(self, value):
        self._hour = value % 12
        self._ampm = 'am' if value <= 12 else 'pm'

obj = Clock(10)
print(obj.hour, obj.ampm)
obj.hour = 14
print(obj.hour, obj.ampm)
