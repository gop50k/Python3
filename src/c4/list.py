# coding: UTF-8
# 内包表記を試すプログラム

data = []
for i in range(1, 6):
    data.append(i * 2)
print(data)

data = [i * 2 for i in range(1, 6)]
print(data)

data = list(map(lambda x : x * 2, range(1, 6)))
print(data)
