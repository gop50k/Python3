# coding: UTF-8
# 抽象基底クラスをテストするプログラム

from abstract-class import MazeRobot
class MazaRobotTest(MazeRobot):

    def __init__(self):
        print('ロボットを初期化します。')

    def choose_dir(self):
        print('前進します。')

robot = MazaRobotTest()
robot.init_robot()
