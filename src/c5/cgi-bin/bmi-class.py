# coding: UTF-8
# BMIを計算するクラス

class bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        print('---')
        print('BMI=', self.bmi)
        b = self.bmi
        if (b < 18.5): print('痩せ型')
        if (b < 25): print('標準')
        if (b < 30): print('肥満(軽)')
        else: print('肥満(重)')

person1 = bmi(65, 175)
person1.printJudge()

person2 = bmi(76, 165)
person2.printJudge()

person3 = bmi(50, 180)
person3.printJudge()
