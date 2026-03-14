#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedRPM
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor


from robot import Robot
from startroutine import StartRoutine
from collection import Collection
from tools import Tools
import time, sys, logging

class Main():
    """
        Hlavní třída programu, odsaď se začne program execution.
        Nedá se moc říct o hlavní třídě co? Hlavně protože je tu zatím fůra hoven :D
    """

    @staticmethod
    def main(args):
        logging.basicConfig(filename='latest.log', level=logging.DEBUG)

        brick = Robot((
            (GyroSensor, INPUT_1, "gyroscope"),
            (MediumMotor, OUTPUT_A, "steering"),
            (LargeMotor, OUTPUT_B, "cradle"),
            (LargeMotor, OUTPUT_C, "acceleration"))
        )
        app = Collection(brick)

        # routine = StartRoutine(brick.getIOByName("gyroscope"), brick.spkr, brick.leds)
        # routine.perform()

        # Wait until we confirm continuation
        brick.leds.set_color('LEFT', 'AMBER'); brick.leds.set_color('RIGHT', 'AMBER') # Technically the semicolon is strongly discouraged by PEP 8 but fuck that 😎
        # pbrick.spkr.play_song((('D4', 's'), ('A4', 's'), ('D5', 'e')))
        steer = brick.getIOByName("steering")
        steer.stop_action = 'hold'
        steer.stop()

        brick.waitUntilPressed()

        app.start()

if __name__ == "__main__":
    Main().main(sys.argv)