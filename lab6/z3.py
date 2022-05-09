import random
from time import time
from texttable import Texttable

from lab6.trees import Trees

if __name__ == '__main__':
	Ns = [50, 100, 500, 1_000, 10_000, 25_000, 50_000, 100_000, 250_000, 1_000_000]

	data = []

	for N in Ns:
		# list of N random floats from 0.00 to 10
		elems_to_insert = [round(random.uniform(.00, 10.00), 2) for _ in range(N)]

		trees = Trees(10)  # generate roots from 0.5 to 10 with step 1

		MULTIPLICATION = 100_000

		insert_start = time()
		for elem in elems_to_insert:
			trees.insert(elem, False)  # insert elems to tree
		insert_end = time()

		min_start = time()
		for i in range(MULTIPLICATION):
			minimum = trees.min(2)  # MIN on third tree
		min_end = time()

		max_start = time()
		for i in range(MULTIPLICATION):
			maximum = trees.max(2)  # MAX on third tree
		max_end = time()

		random_float = round(random.uniform(.0, 10.00), 2)

		search_start = time()
		for i in range(MULTIPLICATION):
			search = trees.search(random_float)
		search_end = time()

		data.append([
			N,
			(insert_end - insert_start),
			(min_end - min_start) / MULTIPLICATION,
			(max_end - max_start) / MULTIPLICATION,
			(search_end - search_start) / MULTIPLICATION
		])

	t = Texttable()
	t.set_precision(8)
	t.add_rows([
		['N', 'insert time', 'find minimum time', 'find maximum time', 'search time'],
		*data
	])
	print(t.draw())

