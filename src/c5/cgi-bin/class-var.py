# coding: UTF-8
# インスタンス変数を利用するクラス

class Cat:
    nakigoe = 'meow'
    def cry(self):
        print(self.nakigoe)

mike = Cat()
nora = Cat()

mike.nakigoe = 'myu'
mike.cry()
nora.cry()
