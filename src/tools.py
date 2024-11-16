class Tools:

    @staticmethod
    def waitUntilPressed(brick):
        while True:
            if brick.buttons.enter:
                break