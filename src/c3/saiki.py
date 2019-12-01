# coding: UTF-8
# 再起処理を記述してみる

def say_hello(i):
    if i <= 0:
        return
    print('ハロー', i)
    say_hello(i - 1)

say_hello(10)
