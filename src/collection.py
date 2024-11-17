from ev3dev2.motor import SpeedRPM, LargeMotor

from field import map
from robot import Robot

import time

class Collection:
    backpack = []
    map = map.Map((0,1))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration") # type: LargeMotor
        cradle = self.brick.getIOByName("cradle") # type: LargeMotor
        init_time = time.time()
        accel.on_for_rotations(SpeedRPM(60), 1)
