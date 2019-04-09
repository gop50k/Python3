# coding: UTF-8
# 遊園地の入場料を計算するプログラム
# 人数の入力
children = int(input("子供料金（１３歳未満）は何人？"))
normal = int(input("通常料金（１４〜６４歳）は何人？"))
elder = int(input("年配者料金（６５〜歳）は何人？"))

# 集計
total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

# 割引対象を確認
if total_num >= 10:
    print("団体割引があります。")
    total_price = total_price * 0.8
else:
    print("団体割引はありません。")

# 結果表示
print("子供料金 :{0}人 × 500円 = {1}円".format(children, children_price))
print("通常料金 :{0}人 × 1000円 = {1}円".format(normal, normal_price))
print("年配者料金 :{0}人 × 700円 = {1}円".format(elder, elder_price))
print("合計 :{0}人 {1}円".format(total_num, total_price))
