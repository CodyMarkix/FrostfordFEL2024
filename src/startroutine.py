from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

import time

class StartRoutine:
    def __init__(self, gyro: GyroSensor, spkr=Sound(), lights=Leds()):
        self.gyro = gyro
        self.spkr = spkr
        self.lights = lights

    def perform(self):
        self.lights.animate_flash('AMBER', sleeptime=0.25)

        self.gyro.calibrate()
        self.lights.animate_stop()
        self.lights.set_color('LEFT', 'GREEN'); self.lights.set_color('RIGHT', 'GREEN') # Technically the semicolon is strongly discouraged by PEP 8 but fuck that 😎
        self.spkr.play_song((('D4', 's'), ('A4', 's'), ('D5', 'e')))
        print(time.time())

        print("Robot is ready for action!")