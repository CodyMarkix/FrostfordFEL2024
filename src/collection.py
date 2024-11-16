from ev3dev2.motor import SpeedRPM

from field import map
from tools import Tools

class Collection:
    backpack = []
    map = map.Map((0,1))

    def __init__(self, brick):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration")
        accel.on_for_seconds(SpeedRPM(50), 10)

        cradle = self.brick.getIOByName("cradle")
        
