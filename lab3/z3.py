from math import sin, sqrt
import random

def definite_integral(a, b, func):
	N = 100000  # number of random points: the bigger => the better result
	dx = b - a  # distance between a & b
	s = 0
	for _ in range(N):
		s += func(random.uniform(a, b))  # get function value at random float from range (a, b)
	s = dx * s / N  # number of points inside rectangle to all points ratio multiplied by distance between a & b
	return s


if __name__ == '__main__':
	print(
		'area of circle with radius of 1 is',
		4 * definite_integral(0, 1, lambda r: sqrt(1 - r * r))
	)

	print(
		'definite integral of sin(x) in range (0, 2) is:',
		definite_integral(0, 2, sin)
	)
