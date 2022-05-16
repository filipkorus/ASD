import csv
from time import time

def naive_matcher(matrix, pattern):
	results = []
	for x in range(len(matrix) - len(pattern) + 1):
		for y in range(len(matrix[x]) - len(pattern) + 1):
			append = True
			for i in range(len(pattern)):
				if pattern[i] != matrix[x][y + i] or pattern[i] != matrix[x + i][y]:
					append = False
					break
			if append:
				results.append((x, y))
	return results

def rabin_karp_matcher_horizontal(text, pattern, d, q):
	n = len(text)
	m = len(pattern)
	h = pow(d, m - 1) % q
	result = set()
	for x in range(n - 2):
		p = 0
		t = 0

		for i in range(m):
			p = (d * p + ord(pattern[i])) % q
			t = (d * t + ord(text[x][i])) % q
		for y in range(n - m + 1):
			if p == t:
				found = True
				for i in range(m):
					if text[x][y + i] != pattern[i]:
						found = False
						break
				if found:
					result.add((x, y))
			if y < n - m:
				t = ((t - h * ord(text[x][y])) * d + ord(text[x][y + m])) % q
	return result

def rabin_karp_matcher_vertical(text, pattern, d, q, result):
	n = len(text)
	m = len(pattern)
	h = pow(d, m - 1) % q

	final_result = set()

	for x in range(n - 2):
		p = 0
		t = 0
		for i in range(m):
			p = (d * p + ord(pattern[i])) % q
			t = (d * t + ord(text[i][x])) % q
		for y in range(n - m + 1):
			if p == t:
				found = True
				for i in range(m):
					if text[y + i][x] != pattern[i]:
						found = False
						break
				if found and (y, x) in result:
					final_result.add((y, x))
			if y < n - m:
				t = ((t - h * ord(text[y][x])) * d + ord(text[y + m][x])) % q

	return list(final_result)

def rabin_karp_matcher(matrix, pattern, d, q):
	results_horizontal = rabin_karp_matcher_horizontal(matrix, pattern, d, q)
	results = rabin_karp_matcher_vertical(matrix, pattern, d, q, results_horizontal)
	# return sorted(results, key=lambda x: x[0])
	return results

if __name__ == '__main__':
	OUTPUT = False
	SAVE_TO_CSV = True
	Ns = [1000, 2000, 3000, 4000, 5000, 8000]

	# save csv header
	if SAVE_TO_CSV:
		with open(file='times.csv', mode='w', newline='') as output_csv_file:
			csv_writer = csv.writer(output_csv_file, delimiter=',')
			csv_writer.writerow([
				'N',
				'naive_time',
				'rabin_karp_time'
			])

	for N in Ns:
		matrix = open(f'./patterns/{N}_pattern.txt').readlines()

		#  naive algorithm
		naive_time_start = time()
		results = naive_matcher(matrix, 'ABC')
		naive_time_end = time()

		if OUTPUT:
			print('NAIVE:')
			for item in results:
				print(item)
			print('\n')

		#  Rabin - Karp algorithm
		rabin_karp_time_start = time()
		results = rabin_karp_matcher(matrix, 'ABC', 16, 13)
		rabin_karp_time_end = time()

		if OUTPUT:
			print('RABIN - KARP:')
			for item in results:
				print(item)
			print('-' * 20)

		if SAVE_TO_CSV:
			with open(file='times.csv', mode='a', newline='') as output_csv_file:
				csv_writer = csv.writer(output_csv_file, delimiter=',')
				csv_writer.writerow([
					N,
					naive_time_end - naive_time_start,
					rabin_karp_time_end - rabin_karp_time_start
				])
