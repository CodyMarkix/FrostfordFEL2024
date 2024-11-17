from robot import Robot

class Tools:
    @staticmethod
    def waitUntilPressed(brick: Robot):
        while True:
            if brick.buttons.enter:
                break