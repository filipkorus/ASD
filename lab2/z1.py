if __name__ == '__main__':
	result = ''
	for i in range(500, 3001):
		if i % 7 == 0 and i % 5 != 0:
			result += str(i)
	print('found', result.count('21'), 'of \'21\'s')
	result = result.replace('21', 'XX')
