# coding: UTF-8
# 抽象基底を実装したプログラム

from abc import ABCMeta, abstractclassmethod

class MazaRobot(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def choose_dir(self):
        pass
