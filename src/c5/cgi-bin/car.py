# coding: UTF-8
# 継承を実装するクラス

class Car:
    def __init__(self, owner):
        self.handle = 0
        self.car_type = 'normal'
        self.owner = owner

    def turn_left(self):
        self.handle -= 90

    def turn_right(self):
        self.handle += 90

    def show_status(self):
        print('---')
        print('owner : ', self.owner)
        print('car_type : ', self.car_type)
        print('handle : ', self.handle)

class Van(Car):
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = 'van'

    def open_door(self):
        print('ドアを開けました。')

    def close_door(self):
        print('ドアを閉めました。')

class Camper(Car):
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = 'camper'

    def make_ice(self):
        print('氷を作成しました。')
