# coding: utf-8
# Caluclation
print(30 + 5)
print(20 * 3)
print(2 * 5 // 3)
print((1 + 2) * 3)
# print(2 ** 9999)

# 花屋の支払い金額を求める
print(((500*18)+(400*6)+(700*16))*0.9)

# 台形の面積を求める
high = 2
low = 5
height = 10 
daikei = (high + low) * height / 2
print(daikei)

# 値段
rore_v = 500
sun_v = 400
tulip_v = 700
# 個数
rose_c = 18
sun_c = 8 - 2
tulip_c = 21 - 5
# 割引率
rate = 0.9
# 計算
sum_v = (rore_v * rose_c) + (sun_v * sun_c) + (tulip_v * tulip_c)
payment = sum_v * rate
# 結果の表示
print('買い物の合計金額は', sum_v, '円です。')
print('割引すると', payment, '円です。')
