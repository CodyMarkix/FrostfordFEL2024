from .ball import Ball
from .depository import Depository
from .angledPlatform import AngledPlatform
from .raisedplatform import RaisedPlatform
from .intersection import Intersection
from .basketball import Basketball
from .coords import Coordinates

class Map:
    """
    ### Coodrinates

    By design, the map follows a "y, x" model, where a coordinate, say (5,6), is Y: 6, X: 5.

    All coordinates are stored in tuples except for `Map.current_position` which is stored in a list.

    ### Layout

    The map is represented in a 2D array

    Diagram: https://media.geeksforgeeks.org/wp-content/uploads/2d_array_init.png

    ### Offset

    Each position on the layout is represented with a tuple.

    An example is this: `(object, offset)` where offset is how many mm it is offset from the centre.

    For most positions this will be 0, but there are exceptions (green balls and basketballs) that need an offset 
    """


    layout = [
            [(Depository(0), 0), (RaisedPlatform(), 0), (AngledPlatform(), 0), (Intersection(13), 0), (Basketball(), -140)],
            [(Ball("blue"), 0), (Ball("red"), 0), (Ball("blue"), 0), (Intersection(15), 0), (Ball("green"), -140)],
            [(Ball("red"), 0), (Ball("blue"), 0), (Ball("red"), 0), (Intersection(15), 0), (Basketball(), -140)],
            [(Ball("blue"), 0), (Ball("red"), 0), (Ball("blue"), 0), (Intersection(15), 0), (Ball("green"), -140)],
            [(Ball("red"), 0), (Ball("blue"), 0), (Ball("red"), 0), (Intersection(15), 0), (Basketball(), -140)],
            [(Depository(1), 0), (RaisedPlatform(), 0), (RaisedPlatform(), 0), (Intersection(14), 0), (Ball("green"), 140)]
    ]

    current_position = Coordinates([0, 1]) # If the position fails to set from the constructor, we use this as a fallback
    def __init__(self, initialPositions):
        self.current_position = Coordinates(list(initialPositions))

    def getObjectByPosition(self, coords):
        return self.layout[coords[1]][coords[0]]
    
    def moveByPosition(self, coords, force=False):
        """
        Moves on map by a certain amount of coordinates. Cannot move diagonally unless `force` is set to True
        """
        if coords[0] * coords[1] == 0 or force:
            if coords[0] > -1 and coords[1] > -1 and coords[0] < len(self.layout[0]) and coords[1] < len(self.layout[1]):
                self.current_position[0] += coords[0]
                self.current_position[1] += coords[1]
            else:
                raise ValueError("Coordinates must be within the map")
        else:
            raise ValueError("Cannot move diagonally")
        
    def setPosition(self, coords):
        self.current_position = Coordinates(list(coords))