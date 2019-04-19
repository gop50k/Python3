# coding: UTF-8
# for 構文でelseを記述してflagの代わりとする
foodstuff = ["Milk", "Banana", "Mango", "Fish", "Nuts"]

for food in foodstuff:
    if food == "Mango":
        print("マンゴーが入っています。")
        break
else:
    print("マンゴーは入っていません。")
