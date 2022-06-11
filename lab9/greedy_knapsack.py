import numpy as np
from check_fit import check_fit
from time import time
import csv

if __name__ == "__main__":
	SAVE_TO_CSV = False
	print('GREEDY ALGORITHM\n')

	# save csv header
	if SAVE_TO_CSV:
		with open(file='greedy_times.csv', mode='w', newline='') as output_csv_file:
			csv_writer = csv.writer(output_csv_file, delimiter=',')
			csv_writer.writerow([
				'N',
				'time',
				'reached_value',
				'max_value'
			])

	for N in [20, 100]:
		# read file
		lines = open(f'./packages/packages{N}.txt').read().splitlines()
		data = []
		for line in lines:
			line = line.split(',')
			try:
				data.append([
					int(line[0]),  # idx
					int(line[1]),  # width
					int(line[2]),  # height
					int(line[3]),  # value
					int(line[3]) / (int(line[1]) * int(line[2]))  # value2
				])
			except ValueError:
				pass

		# sort by value2 desc
		data.sort(key=lambda x: -x[4])

		# empty knapsack
		knapsack = np.zeros((N, N), dtype=int)
		value = 0
		start = time()

		for item in data:
			fit = check_fit(item[1], item[2], knapsack)
			if fit:
				# x,y placement
				if (fit[2]):   # x_start   width + x_start
					for x in range(fit[0], item[1] + fit[0]):
						#             y_start   height + y_start
						for y in range(fit[1], item[2] + fit[1]):
							knapsack[y][x] = item[0]  # insert item with `id` to knapsack
				# y,x placement
				else:
					for x in range(fit[0], item[1] + fit[0]):
						for y in range(fit[1], item[2] + fit[1]):
							knapsack[x][y] = item[0]  # insert item with `id` to knapsack

				value += item[3]

		# value of all elements
		max_value = 0
		for item in data:
			max_value += item[3]

		print(knapsack)
		elapsed_time = time() - start
		print(f'size = {N}')
		print(f'time = {elapsed_time}')
		print(f'reached value = {value}')
		print(f'max possible value = {max_value}\n')

		if SAVE_TO_CSV:
			with open(file='greedy_times.csv', mode='a', newline='') as output_csv_file:
				csv_writer = csv.writer(output_csv_file, delimiter=',')
				csv_writer.writerow([
					N,
					elapsed_time,
					value,
					max_value
				])
