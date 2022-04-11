import copy
import random
from time import time
from texttable import Texttable

def insertion_sort(A: list) -> None:
	for i in range(1, len(A)):
		x = A[i]
		j = i - 1
		while j >= 0 and A[j] > x:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = x

def merge_sort(A: list, start: int, end: int) -> None:
	if start < end:
		mid = (start + end) // 2
		merge_sort(A, start, mid)
		merge_sort(A, mid + 1, end)
		merge(A, start, mid, end)

def merge(A: list, start: int, mid: int, end: int) -> None:
	tmp = []
	i = start
	j = mid + 1

	while i <= mid and j <= end:
		if A[i] <= A[j]:
			tmp.append(A[i])
			i += 1
		else:
			tmp.append(A[j])
			j += 1

	while i <= mid:
		tmp.append(A[i])
		i += 1

	while j <= end:
		tmp.append(A[j])
		j += 1

	for i in range(start, end + 1):
		A[i] = tmp[i - start]

def random_list(start: int, end: int, length: int) -> list:
	return [random.randint(start, end) for _ in range(length)]

if __name__ == '__main__':
	ins_sort_times, merge_sort_times, python_sort_times = [], [], []

	AMOUNT_OF_ITERATIONS = 10**2
	RANDOM_LIST_SIZE = 10**4

	for _ in range(AMOUNT_OF_ITERATIONS):
		mylist = random_list(0, 100, RANDOM_LIST_SIZE)
		mylist2 = copy.deepcopy(mylist)
		mylist3 = copy.deepcopy(mylist)

		start = time()
		insertion_sort(mylist)
		ins_sort_times.append(time() - start)

		start = time()
		merge_sort(mylist2, 0, len(mylist2) - 1)
		merge_sort_times.append(time() - start)

		start = time()
		mylist3.sort()
		python_sort_times.append(time() - start)

	t = Texttable()
	t.add_rows([
		['SORT TYPE', 'SUM TIME', 'MIN TIME', 'MAX TIME', 'AVG TIME'],
		['insertion', sum(ins_sort_times), min(ins_sort_times), max(ins_sort_times), sum(ins_sort_times) / len(ins_sort_times)],
		['merge', sum(merge_sort_times), min(merge_sort_times), max(merge_sort_times), sum(merge_sort_times) / len(merge_sort_times)],
		['python', sum(python_sort_times), min(python_sort_times), max(python_sort_times), sum(python_sort_times) / len(python_sort_times)]
	])
	print(f'Amount of iterations = {AMOUNT_OF_ITERATIONS}')
	print(f'Random list size = {RANDOM_LIST_SIZE}')
	print(t.draw())
