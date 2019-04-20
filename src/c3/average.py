# coding: UTF-8
# テストの合計点を算出するプログラム
points = [77, 67, 97, 76, 22, 100]

sum_v = 0
for i in points:
    sum_v += i
    print(i, "点を足して合計は", sum_v)

ave_v = sum_v / len(points)
print(ave_v)

# fix
sum_v = sum(points)
ave_v = sum_v / len(points)
print("all sum", sum_v)
print("average", ave_v)
