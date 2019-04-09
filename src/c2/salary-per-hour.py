# coding: UTF-8
# 時給計算プログラム
user = input("時給はいくらですか？")
jikyu = int(user)

user = input("一日何時間働きましたか？")
hour = int(user)

user = input("月何日働きましたか？")
day = int(user)

salary = jikyu * hour * day

fmt = """
時給{0}円で、一日{1}時間働いて、月{2}日働いたので...
給料は{3}円です！Yeah！
"""

desc = fmt.format(jikyu, hour, day, salary)
print(desc)
