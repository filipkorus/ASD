from math import sin
import random

def def_integral(a, b, is_inside, R):
	N = 1000000
	s = 0
	for _ in range(N):
		x = random.uniform(a, b)
		y = random.uniform(-R, R)
		if is_inside(x, y):
			s += 1
	return 2 * R * (b - a) * s / N


if __name__ == '__main__':
	radius = 1
	print(
		f'area of circle with radius of {radius} is',
		2 * def_integral(0, radius, lambda x, y: x**2 + y**2 < radius**2, radius)
	)

	print(
		'definite integral of sin(x) in range (0, 2) is',
		def_integral(0, 2, lambda x, y: sin(x) > y > 0, 1)
	)
