class Intersection:
    """
    ### Directions

    Directions are encoded in 4 bits.
    #### Example
    
    `0010`

    - 0 = Left
    - 0 = Right
    - 1 = Up
    - 0 = Down

    Unfortunately Python can't store 4 bit numbers as is so... either learn binary or use a binary to int converter :P
    """
    def __init__(self, directions):
        self.directions = directions