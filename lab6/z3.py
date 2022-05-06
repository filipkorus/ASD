import random

from lab6.trees import Trees

if __name__ == '__main__':
	# list of 500 random floats from 0.00 to 100.00
	elems_to_insert = [round(random.uniform(.0, 100.0), 2) for _ in range(500)]

	trees = Trees(101)  # roots will be generated from 0.5 to 101 with step 1
	for elem in elems_to_insert:
		trees.insert(elem)  # insert to tree

	# trees.print()

	print(
		f'min = {trees.min()}',
		f'max = {trees.max()}',
		trees.search(21.37),
		sep='\n'
	)
