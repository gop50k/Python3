# coding: UTF-8
# forのネストで数字の組み合わせを表示するプログラム

result = []
base = [1, 2, 3]

for x in base:
    for y in base:
        result.append((x, y))
print(result)

base = [1, 2, 3]
result = [(x, y) for x in base for y in base if x != y]
print(result)
