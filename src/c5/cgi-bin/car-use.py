# coding: UTF-8
# 継承を利用するクラス

import car

car1 = car.Van('Taro')
car1.turn_left()
car1.show_status()

car2 = car.Camper('Jiro')
car2.turn_right()
car2.show_status()
car2.make_ice()
