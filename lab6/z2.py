from lab6.trees import Trees

if __name__ == '__main__':
	elems_to_insert = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]

	trees = Trees()
	for elem in elems_to_insert:
		trees.insert(elem)  # INSERT

	# trees.print()

	print(
		f'min = {trees.min(2)}',  # MIN on third tree
		f'max = {trees.max(2)}',  # MAX on third tree
		trees.search(7.7),  # SEARCH
		sep='\n'
	)
