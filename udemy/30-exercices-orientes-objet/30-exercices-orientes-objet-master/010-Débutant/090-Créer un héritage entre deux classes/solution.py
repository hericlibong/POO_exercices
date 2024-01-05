class Shape:
    def __init__(self):
        self.x = 0
        self.y = 0


class Cube(Shape):
    def __init__(self):
        super().__init__()
        self.z = 0

cube = Cube()
print(cube.x)
print(cube.y)
print(cube.z)