from ev3dev2.motor import SpeedRPM, SpeedPercent, MediumMotor, LargeMotor
from ev3dev2.sensor.lego import UltrasonicSensor
from field.ball import Ball
from field.basketball import Basketball

from field import map
from robot import Robot
from tools import Tools

import time, logging

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

        iter = 0
        init_time = time.time()
        logging.info(init_time)
        while iter < 4:
            logging.info("Iteration: " + str(iter))
            if iter != 0:

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(56) * -1), block=True)
                time.sleep(0.5)
                
                steer.on_for_degrees(SpeedRPM(200), 45, block=True)
                time.sleep(0.5)

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(40) * -1), block=True)
                self.map.moveByPosition((-1, 0))
                self.map.moveByPosition((0, 1))
                time.sleep(0.5)

                cradle.on_for_degrees(20, -80, block=True)
                time.sleep(1)

                steer.on_for_degrees(SpeedRPM(200), -45, block=True)

                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(112 - 28 * iter) * - 1), block=True)

                steer.on_for_degrees(SpeedRPM(200), 45, block=True)
                time.sleep(0.5)
                self.map.moveByPosition((1, 0))
                self.map.moveByPosition((0, -1))

                # steer.on_for_degrees(SpeedRPM(200), -45, block=True)
                accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(43), block=True)
                time.sleep(0.5)

                steer.on_for_degrees(SpeedRPM(200), -45, block=True)
                accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(12) * -1), block=True)
                time.sleep(0.5)
                logging.info("balls")
                logging.info("cum")


            # steer.on_for_degrees(SpeedRPM(200), -90, block=True)
            accel.on_for_rotations(SpeedRPM(60), self.brick.cmToRotations(74), block=True)
            
            logging.info("Should now be at y: 1; x: 2")

            self.backpack[0 if iter % 2 == 0 else 1].update({"color": "blue", "count": self.backpack[0 if iter % 2 == 0 else 1]["count"] + 1})
            self.backpack[1 if iter % 2 == 0 else 0].update({"color": "blue", "count": self.backpack[1 if iter % 2 == 0 else 0]["count"] + 1})
            self.backpack[0 if iter % 2 == 0 else 1].update({"color": "red", "count": self.backpack[0 if iter % 2 == 0 else 1]["count"] + 1})
            self.map.moveByPosition((0, -2))

            logging.info("Should now be at y: 1; x: 0")
            time.sleep(0.5)
            accel.on_for_rotations(SpeedRPM(60), -0.100, block=True)


            cradle.on_for_degrees(10, 60, block=True)

            accel.on_for_rotations(SpeedRPM(60), (self.brick.cmToRotations(43) * -1), block=True)

            logging.info("Should now be at y: 1; x: 2")
            time.sleep(0.5) # Should now be at y: 1; x: 2

            steer.on_for_degrees(SpeedRPM(200), 45, block=True)
            accel.on_for_rotations(SpeedRPM(70), (self.brick.cmToRotations(37) * - 1), block=True)
            self.map.moveByPosition((-1, 0))
            self.map.moveByPosition((0, 1))

            logging.info("Should now be at y: 0; x: 3")
            time.sleep(1) # Should now be at y: 0; x: 3

            # Correction on backing out
            steer.on_for_degrees(SpeedRPM(200), -63, block=True)
            accel.on_for_rotations(SpeedRPM(70), self.brick.cmToRotations(15), block=True)
            steer.on_for_degrees(SpeedRPM(200), 18.5, block=True)

            time.sleep(0.5)

            # ysteer.on_for_degrees(SpeedRPM(200), -46, block=True)
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(112 if iter == 0 else 112 - 28 * iter), block=True)
            self.map.moveByPosition((0, 4))
            logging.info("should now be at: y: 4, x: 3")
            
            time.sleep(0.5)

            steer.on_for_degrees(SpeedRPM(200), 45, block=True)
            time.sleep(0.25)
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(40), block=True)
            self.map.moveByPosition((1, 0))
            self.map.moveByPosition((0, -1)) # Should now be at: y: 5; x: 2
            logging.info("Should now be at: y: 5; x: 2")

            steer.on_for_degrees(SpeedRPM(200), -45, block=True)
            accel.on_for_rotations(SpeedRPM(80), self.brick.cmToRotations(56), block=True)
            self.map.moveByPosition((0, 1)) # Should now be at y: 5; x: 1

            logging.info("Should now be at y: 5; x: 1")
            time.sleep(0.5)

            cradle.on_for_degrees(10, 30)
            time.sleep(2)
            
            iter += 1

        accel.on_for_rotations(SpeedRPM(80), (self.brick.cmToRotations(28) * -1), block=True)


        logging.info("TOOK: " + str(time.time() - init_time) + "s")