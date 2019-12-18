# coding: UTF-8
# fizzbuzzを内包表記でやるプログラム

res = [
    "Fizz Buzz" if i % 15==0 else "Fizz"
                if i %3==0 else "Buzz"
                if i %5==0 else str(i)
    for i in range(i, 21)]

print("¥n".join(res))
