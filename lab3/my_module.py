from math import sqrt

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius * self.radius

	def perimeter(self):
		return 2 * 3.14 * self.radius


class Triangle:
	def __init__(self, a, b, c):
		self.a, self.b, self.c = a, b, c

	def area(self):
		p = (self.a + self.b + self.c) / 2
		return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

	def perimeter(self):
		return self.a + self.b + self.c

class Square:
	def __init__(self, a):
		self.a = a

	def area(self):
		return self.a * self.a

	def perimeter(self):
		return 4 * self.a
