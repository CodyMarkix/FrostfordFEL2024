from ev3dev2.motor import SpeedRPM

from field import map
from robot import Robot
from tools import Tools

class Collection:
    backpack = []
    map = map.Map((0,1))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration")
        # accel.on_for_seconds(SpeedRPM(50), 10)
        
        accel.on_for_rotations(SpeedRPM(50), )
        
