from time import time
from texttable import Texttable


def hanoi(n: int, src: ..., buff: ..., dest: ..., output: bool = True) -> None:
	"""
	:param output: set to False disables printing
	:param dest: destination stack identifier
	:param buff: buffer stack identifier
	:param src: source stack identifier
	:param n: amount of disks on source stack
	"""
	if n > 0:
		hanoi(n - 1, src, dest, buff, output)
		if output:
			print(src, '->', dest)
		hanoi(n - 1, buff, src, dest, output)

def hanoi_iter(n: int, src: ..., buff: ..., dest: ..., output: bool = True) -> None:
	"""
	:param output: set to False disables printing
	:param dest: destination stack identifier
	:param buff: buffer stack identifier
	:param src: source stack identifier
	:param n: amount of disks on source stack
	"""
	if n % 2 == 0:
		dest, buff = buff, dest

	src_stack = [i for i in range(n)]
	buff_stack = []
	dest_stack = []

	for i in range(1, 2 ** n):
		if i % 3 == 1:
			if move(src_stack, dest_stack):
				if output:
					print(src, '->', dest)
			else:
				if output:
					print(dest, '->', src)
		if i % 3 == 2:
			if move(src_stack, buff_stack):
				if output:
					print(src, '->', buff)
			else:
				if output:
					print(buff, '->', src)
		if i % 3 == 0:
			if move(buff_stack, dest_stack):
				if output:
					print(buff, '->', dest)
			else:
				if output:
					print(dest, '->', buff)

def move(A: list, B: list) -> bool:
	"""
	moves between A and B or otherwise\n
	:return: True if move was from A to B else False
	"""
	if not A:  # if A is empty
		A.insert(0, B.pop(0))  # place top disk of B to top of A stack
		return False
	elif not B:  # if B is empty
		B.insert(0, A.pop(0))
		return True
	else:
		if A[0] < B[0]:  # if A's top disk is smaller than B's top disk
			B.insert(0, A.pop(0))
			return True
		else:
			A.insert(0, B.pop(0))
			return False

if __name__ == '__main__':
	data = []

	for N in range(5, 31, 5):
		rec_time_start = time()
		hanoi(N, 'src', 'buff', 'dest', False)
		rec_time_end = time()

		iter_time_start = time()
		hanoi_iter(N, 'src', 'buff', 'dest', False)
		iter_time_end = time()

		data.append([
			N,
			rec_time_end - rec_time_start,
			iter_time_end - iter_time_start
		])

	t = Texttable()
	t.add_rows([
		['number of disks', 'recursive time', 'iterative time'],
		*data
	])
	print(t.draw())
