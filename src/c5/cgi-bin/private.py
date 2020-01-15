# coding: UTF-8
# プライベートメソッドを確認するクラス

class Game:
    def __goal(self):
        print('非公開のメソッド')

    def play(self):
        print('公開のメソッド')

game = Game()
game.play()
game.__goal()
