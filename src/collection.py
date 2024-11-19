from ev3dev2.motor import SpeedRPM, SpeedPercent, MediumMotor, LargeMotor
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
    map = map.Map((0,2))

    def __init__(self, brick: Robot):
        self.brick = brick

    def start(self):
        accel = self.brick.getIOByName("acceleration") # type: LargeMotor
        cradle = self.brick.getIOByName("cradle") # type: LargeMotor
        steer = self.brick.getIOByName("steering") # type: MediumMotor
        ultras = self.brick.getIOByName("ultrasonic") # type: UltrasonicSensor

        init_time = time.time()
        

        # steer.on_for_degrees(SpeedRPM(200), -90, block=True)
        # accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(12), block=True)
        # self.map.moveByPosition((-1, 0))
        # self.map.moveByPosition((0, -1))
        # self.backpack[1].update({"color": "red", "count": self.backpack[1]["count"] + 1})


        # steer.on_for_degrees(SpeedRPM(200), 90, block=True)
        # accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(26), block=True)
        # self.map.moveByPosition((0, -1))
        # self.backpack[0].update({"color": "blue", "count": self.backpack[0]["count"] + 1})


        # steer.on_for_degrees(SpeedRPM(200), 45)
        # accel.on_for_rotations(SpeedRPM(120), self.brick.cmToRotations(32), block=True)
        # self.backpack[1].update({"color": "blue", "count": self.backpack[1]["count"] + 1})

        iter = 0
        while iter < 1:
            print("Iteration: " + str(iter))
            if iter != 0:
                cradle.on_for_degrees(60, -80, block=True)
                time.sleep(0.25)

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(28) * -1), block=True)
                self.brick.waitUntilPressed()
                
                steer.on_for_degrees(SpeedRPM(200), 90, block=True)
                time.sleep(0.25)

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(18) * - 1), block=True)
                self.map.moveByPosition((-1, 0))
                self.map.moveByPosition((0, 1))
                self.brick.waitUntilPressed()

                steer.on_for_degrees(SpeedRPM(200), -90, block=True)

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(112 - 28 * iter) * - 1), block=True)

                steer.on_for_degrees(SpeedRPM(200), 90, block=True)
                time.sleep(0.25)
                self.map.moveByPosition((1, 0))
                self.map.moveByPosition((0, -1))


            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(18), block=True)

            # steer.on_for_degrees(SpeedRPM(200), -90, block=True)
            self.backpack[0 if iter % 2 == 0 else 1].update({"color": "blue", "count": self.backpack[0 if iter % 2 == 0 else 1]["count"] + 1})
            
            print("Should now be at y: 1; x: 2")

            accel.on_for_rotations(SpeedRPM(60), self.brick.cmToRotations(56), block=True)
            self.backpack[1 if iter % 2 == 0 else 0].update({"color": "blue", "count": self.backpack[1 if iter % 2 == 0 else 0]["count"] + 1})
            self.backpack[0 if iter % 2 == 0 else 1].update({"color": "red", "count": self.backpack[0 if iter % 2 == 0 else 1]["count"] + 1})
            self.map.moveByPosition((0, -2))

            print("Should now be at y: 1; x: 0")
            time.sleep(0.5)
            accel.on_for_rotations(SpeedRPM(60), -0.125, block=True)


            cradle.on_for_degrees(10, 60, block=True)

            accel.on_for_rotations(SpeedRPM(60), (self.brick.cmToRotations(40) * -1), block=True)

            print("Should now be at y: 1; x: 2")
            time.sleep(0.5) # Should now be at y: 1; x: 2

            steer.on_for_degrees(SpeedRPM(200), 45, block=True)
            accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(84) * - 1), block=True)
            self.map.moveByPosition((-1, 0))
            self.map.moveByPosition((0, 1))

            print("Should now be at y: 0; x: 3")
            time.sleep(1) # Should now be at y: 0; x: 3

            steer.on_for_degrees(SpeedRPM(200), -46, block=True)
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(112), block=True)
            self.map.moveByPosition((0, 4))
            
            time.sleep(0.5)

            steer.on_for_degrees(SpeedRPM(200), 45, block=True)
            time.sleep(0.25)

            print("Should now be at: y: 5; x: 2")
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(18), block=True)
            self.map.moveByPosition((1, 0))
            self.map.moveByPosition((0, -1)) # Should now be at: y: 5; x: 2

            steer.on_for_degrees(SpeedRPM(200), -45, block=True)
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(14), block=True)
            self.map.moveByPosition((0, 1)) # Should now be at y: 5; x: 1

            print("Should now be at y: 5; x: 1")
            time.sleep(0.5)

            cradle.on_for_degrees(10, 20)
            time.sleep(5)
            
            iter += 1

        accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(56) * -1), block=True)

        
    
