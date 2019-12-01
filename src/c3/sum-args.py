# coding: UTF-8
# 可変長の引数を処理する関数

def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v

# 合計表示
print(sumArgs(1, 2, 3))
print(sumArgs(1, 2, 3, 4, 5))
print(sumArgs(1, 2, 3, 44, 455, 5555))
