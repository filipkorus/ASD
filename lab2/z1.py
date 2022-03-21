if __name__ == '__main__':
	result = ''
	for i in range(504, 3001, 7):
		if i % 5 != 0:
			result += str(i)
	print('found', result.count('21'), 'of \'21\'s')
	result = result.replace('21', 'XX')
