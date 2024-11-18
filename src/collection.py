from ev3dev2.motor import SpeedRPS, MediumMotor, LargeMotor
from ev3dev2.sensor.lego import UltrasonicSensor

from field import map
from robot import Robot
from tools import Tools

import time

class Collection:
    backpack = []
    map = map.Map((0,1))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration") # type: LargeMotor
        cradle = self.brick.getIOByName("cradle") # type: LargeMotor
        steer = self.brick.getIOByName("steering") # type: MediumMotor
        ultras = self.brick.getIOByName("ultrasonic") # type: UltrasonicSensor

        init_time = time.time()
        
        # accel.on_for_rotations(SpeedRPM(60), 6.72, block=True)
        # print(cradle)
        # cradle.on_for_degrees(SpeedRPM(60), 40)

        # self.brick.turnAround(accel, steer, self.brick.getIOByName("gyroscope"))

        accel.on_for_seconds(SpeedRPS(2.3), 4, block=False)
        while True:
            print(accel.is_overloaded, accel.is_stalled)