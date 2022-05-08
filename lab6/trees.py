import numpy as np
from lab6.bst import BST

class Trees:
	def __init__(self, max_element=10):
		self.tree_list = [BST(i) for i in np.arange(0.5, max_element, 1)]

	def insert(self, value):
		for i, tree in enumerate(self.tree_list):
			if abs(value - tree.root.value) <= 0.5:
				tree.insert(value)
				return self

	def min(self):
		return self.tree_list[0].min()

	def max(self):
		return self.tree_list[-1].max()

	def search(self, value):
		for tree in self.tree_list:
			if abs(tree.root.value - value) <= 0.5:
				return tree.search(tree.root, value)
		return False

	def print(self):
		print('-' * 15, end='')
		for tree in self.tree_list:
			tree.print()
			print('-' * 15, end='')
		print()
		return self
