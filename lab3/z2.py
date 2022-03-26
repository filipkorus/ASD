from lab3.my_module import Circle, Triangle, Square

if __name__ == '__main__':
	circle = Circle(1)
	print(circle.area(), circle.perimeter())

	triangle = Triangle(3, 4, 5)
	print(triangle.area(), triangle.perimeter())

	square = Square(5)
	print(square.area(), square.perimeter())
