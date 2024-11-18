from ev3dev2.motor import SpeedRPM, MediumMotor, LargeMotor
from ev3dev2.sensor.lego import UltrasonicSensor
from field.ball import Ball
from field.basketball import Basketball

from field import map
from robot import Robot
from tools import Tools

import time

class Collection:
    backpack = [
        {"color": "blue", "count": 0},
        {"color": "red", "count": 0}    
    ]
    map = map.Map((4,3))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration") # type: LargeMotor
        cradle = self.brick.getIOByName("cradle") # type: LargeMotor
        steer = self.brick.getIOByName("steering") # type: MediumMotor
        ultras = self.brick.getIOByName("ultrasonic") # type: UltrasonicSensor

        init_time = time.time()
        

        steer.on_for_degrees(SpeedRPM(200), -45, block=True)
        accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(28), block=True)
        self.map.moveByPosition((-1, 0))
        self.map.moveByPosition((0, -1))
        self.backpack[1].update({"color": "red", "count": self.backpack[1]["count"] + 1})


        steer.on_for_degrees(SpeedRPM(200), 45, block=True)
        accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(26), block=True)
        self.map.moveByPosition((0, -1))
        self.backpack[0].update({"color": "blue", "count": self.backpack[0]["count"] + 1})


        steer.on_for_degrees(SpeedRPM(200), 45)
        accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(32), block=True)
        self.backpack[1].update({"color": "blue", "count": self.backpack[1]["count"] + 1})

