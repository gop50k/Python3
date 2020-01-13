# coding: UTF-8
# オーバーライドを利用するクラス

class SuperClass:
    def hoge(self, id):
        print('---')
        print('SuperClass.hoge=', id)

class SubClass(SuperClass):
    def hoge(self, id):
        super().hoge(id)
        print('SubClass.hoge=', id)

rc = SuperClass()
rc.hoge(100)

sc = SubClass()
sc.hoge(300)
