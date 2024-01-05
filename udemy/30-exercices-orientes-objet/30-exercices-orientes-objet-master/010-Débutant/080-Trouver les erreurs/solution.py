class Geometry:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

sphere = Geometry(x=9, y=2, z=5)
print(sphere.x)
print(sphere.y)
print(sphere.z)