import pandas as pd
from lab6.node import Node

class BST:
	def __init__(self, root=None):
		self.root = None if root is None else Node(root)
		self.idx = None

	def insert(self, value, output=True):
		if self.root is None:
			self.root = Node(value)
		else:
			def _insert(value, curr_node, output):
				if value < curr_node.value:
					if curr_node.left is None:
						curr_node.left = Node(value)
					else:
						_insert(value, curr_node.left, output)
				elif value > curr_node.value:
					if curr_node.right is None:
						curr_node.right = Node(value)
					else:
						_insert(value, curr_node.right, output)
				else:
					if output:
						print('Value already in tree! Skipping...')
			_insert(value, self.root, output)

	def height(self):
		if self.root is None:
			return 0
		else:
			def _height( curr_node, curr_height):
				if curr_node is None:
					return curr_height
				left_height = _height(curr_node.left, curr_height + 1)
				right_height = _height(curr_node.right, curr_height + 1)
				return max(left_height, right_height)
			return _height(self.root, 0)

	def print(self):
		if self.root is not None:
			arr = [[] for _ in range(self.height())]
			self.idx = 0

			def _print(curr_node, arr):
				if curr_node is not None:
					try:
						arr[self.idx].append('-' * len(arr[self.idx]) + ' ' + str(curr_node.value))
					except IndexError:
						arr.append([])
						arr[self.idx].append('-' * len(arr[self.idx]) + ' ' + str(curr_node.value))
					if curr_node.left is None:
						if curr_node.right is None:
							self.idx += 1
							for _ in range(self.idx):
								if self.idx >= self.height():
									return
								arr[self.idx].append('')
					_print(curr_node.left, arr)
					_print(curr_node.right, arr)
			_print(self.root, arr)
			max_length = max(len(x) for x in arr)
			for i, line in enumerate(arr):
				while len(arr[i]) < max_length:
					arr[i].append('')

			self.idx = None
			df = pd.DataFrame(arr, ['' for _ in range(len(arr))], ['' for _ in range(max_length)])
			print(df)

	def max(self):
		curr_node = self.root
		while curr_node.right is not None:
			curr_node = curr_node.right
		return curr_node.value

	def min(self):
		curr_node = self.root
		while curr_node.left is not None:
			curr_node = curr_node.left
		return curr_node.value

	def search(self, curr_node, value):
		if value < curr_node.value:
			if curr_node.left is None:
				return False
			return self.search(curr_node.left, value)
		elif value > curr_node.value:
			if curr_node.right is None:
				return False
			return self.search(curr_node.right, value)
		else:
			return True
