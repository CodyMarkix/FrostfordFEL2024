from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedRPM
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.led import Leds

from tools import Tools

import time, math

class Robot:
    io_list = []
    
    def __init__(self, iomap):
        self.__initIO__(iomap)
        self.buttons = Button()
        self.leds = Leds()
        self.spkr = Sound()

    def __initIO__(self, iomap):
        for entry in iomap:
            # Example iomap entry: (ColorSensor, 'in1', 'name'); We're going around the abstraction given to us
            # because the way this library is done is fucking stupid
            self.io_list.append({"name": entry[2], "object": entry[0](entry[1])}) # type: ignore

        self.io_list.sort(key=lambda x: x["name"])

    def getIOByName(self, target):
        """
        Searches for a registered sensor/motor by its name.

        https://en.wikipedia.org/wiki/Binary_search#Algorithm
        
        I know this looks complicated but it's faster than linear search and we
        can't afford to lose seconds here.
        """
        low = 0
        high = len(self.io_list) - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_value = self.io_list[mid]["name"]
            
            if mid_value == target:
                return self.io_list[mid]["object"]
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return None
    
    def turnAround(self, accel: LargeMotor, steer: MediumMotor, gyro: GyroSensor):
        steer.reset()
        
        
        steer.on_for_degrees(SpeedRPM(50), 45, block=True)
        time.sleep(0.2)

        accel.on_for_rotations(SpeedRPM(50), 0.2, block=True)
        time.sleep(0.2)
            
        while gyro.angle < 180:
            print(gyro.angle)
            steer.on_for_degrees(SpeedRPM(50), -90, block=True)
            time.sleep(0.2)

            accel.on_for_rotations(SpeedRPM(50), -0.2, block=True)
            time.sleep(0.2)
            
            print(gyro.angle)
            steer.on_for_degrees(SpeedRPM(50), 90, block=True)
            time.sleep(0.2)

            accel.on_for_rotations(SpeedRPM(50), 0.2, block=True)
            time.sleep(0.2)


        steer.reset()

    def cmToRotations(cm: float, s: float) -> float:
        """
        Convert path in cm to rotations
        """
        wheel_perimeter = round(4 * math.pi, 2)

        return cm / wheel_perimeter
    
    def waitUntilPressed(self):
        while True:
            if self.buttons.enter:
                break