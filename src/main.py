#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedRPM
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor


from robot import Robot
from startroutine import StartRoutine
from collection import Collection
from tools import Tools
import time, sys

class Main():
    """
        Hlavní třída programu, odsaď se začne program execution.
        Nedá se moc říct o hlavní třídě co? Hlavně protože je tu zatím fůra hoven :D
    """

    @staticmethod
    def main(args):
        brick = Robot((
            (GyroSensor, INPUT_1, "gyroscope"),
            (UltrasonicSensor, INPUT_2, "ultrasonic"),
            (MediumMotor, OUTPUT_A, "steering"),
            (LargeMotor, OUTPUT_B, "cradle"),
            (LargeMotor, OUTPUT_C, "acceleration"))
        )
        app = Collection(brick)

        routine = StartRoutine(brick.getIOByName("gyroscope"), brick.spkr, brick.leds)
        routine.perform()

        # Wait until we confirm continuation
        brick.waitUntilPressed()

        app.start()

if __name__ == "__main__":
    Main().main(sys.argv)