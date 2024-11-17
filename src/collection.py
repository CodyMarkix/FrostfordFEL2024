from ev3dev2.motor import SpeedRPM, LargeMotor

from field import map
from robot import Robot
from tools import Tools

class Collection:
    backpack = []
    map = map.Map((0,1))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration") # type: LargeMotor
        cradle = self.brick.getIOByName("cradle") # type: LargeMotor
        
