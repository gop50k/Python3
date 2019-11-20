# coding: UTF-8
# 印税を計算するプログラム
def calc_royalty(price, sales, per):
    rate = per / 100 #印税率
    ro = int(price * sales * rate)
    return ro

i = input('定価は？')
price = int(i)

i = input('発行部数は？')
sales = int(i)

i = input('印税率は？')
per = float(i)

v = calc_royalty(price, sales, per)
print('印税は', v ,'円です。')
