from time import time

if __name__ == '__main__':
	text = input('Insert a string: ').strip().lower()
	start = time()
	if text.count(' ') == 0:
		print('String contains one word')
		with open('SJP.txt') as file:
			dictionary = [line.rstrip() for line in file]
		print(f"Dictionary {'' if text in dictionary else 'not '}includes given word")
		print('Execution time:', time() - start)
	else:
		print('Sting contains more than one word')


