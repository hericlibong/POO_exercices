class Cube:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

cube = Cube()
cube.set_position(1, 2, 3)