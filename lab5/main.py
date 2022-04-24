from time import time
from texttable import Texttable

def hanoi(n: int, src: str, buff: str, dest: str, output: bool = True) -> None:
	if n > 0:
		hanoi(n - 1, src, dest, buff, output)
		if output:
			print(src, '->', dest)
		hanoi(n - 1, buff, src, dest, output)

def hanoi_iter(n: int, src: str, buff: str, dest: str, output: bool = True) -> None:
	if n % 2 == 0:
		dest, buff = buff, dest

	src_stack = [i for i in range(n, 0, -1)]
	buff_stack = []
	dest_stack = []

	for i in range(1, 2**n):
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

def move(a: list, b: list) -> bool:
	"""
	:return:
	True if move was from a to b else False
	"""
	if not a:  # if a is empty
		tmp = b[-1]
		b.pop()
		a.append(tmp)
		return False
	elif not b:  # if b is empty
		tmp = a[-1]
		a.pop()
		b.append(tmp)
		return True
	else:
		if a[-1] < b[-1]:  # if a's top disk is smaller than b's top disk
			tmp = a[-1]
			a.pop()
			b.append(tmp)
			return True
		else:
			tmp = b[-1]
			b.pop()
			a.append(tmp)
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
	
