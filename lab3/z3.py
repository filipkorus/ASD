from math import sin
import random

def def_integral(a, b, is_inside):
	N = 1000000
	s = 0
	for _ in range(N):
		x = random.uniform(a, b)
		y = random.uniform(-5, 5)
		if is_inside(x, y):
			s += 1
	return (b - a) * 10 * s / N

if __name__ == '__main__':
	print(
		'area of circle with radius of 1 is',
		2 * def_integral(0, 1, lambda x, y: x**2 + y**2 < 1)
	)

	print(
		'definite integral of sin(x) in range (0, 2) is',
		def_integral(0, 2, lambda x, y: sin(x) > y > 0)
	)
