#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4

from ev3dev2.motor import LargeMotor, MediumMotor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor


from robot import Robot
from startroutine import StartRoutine
from collection import Collection
from tools import Tools
import time

class Main():
    """
        Hlavní třída programu, odsaď se začne program execution.
        Nedá se moc říct o hlavní třídě co? Hlavně protože je tu zatím fůra hoven :D
    """

    @staticmethod
    def main():
        brick = Robot((
            (GyroSensor, INPUT_1, "gyroscope"),
            (ColorSensor, INPUT_4, "colorCam"),
            (MediumMotor, OUTPUT_A, "steering"),
            (LargeMotor, OUTPUT_B, "cradle"),
            (LargeMotor, OUTPUT_C, "acceleration"))
        )
        app = Collection(brick)

        routine = StartRoutine(brick.getIOByName("gyroscope"), brick.getIOByName("colorCam"), brick.spkr, brick.leds)
        routine.perform()

        # Wait until we confirm continuation
        Tools.waitUntilPressed(brick)

        app.start()


if __name__ == "__main__":
    print(time.time())
    Main().main()