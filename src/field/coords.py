class Coordinates(list):
    def __str__(self):
        return "X: " + str(self[0]) + "; Y: " + str(self[1])