from time import time

if __name__ == '__main__':
	text = input('Insert a string: ').strip().lower()
	start = time()
	if text.count(' ') == 0:
		print('String contains one word')
		dictionary = open('SJP.txt', encoding='utf-8').read().splitlines()
		print(f"Dictionary {'' if text in dictionary else 'not '}includes given word")
		print('Execution time:', time() - start)
	else:
		print('String contains more than one word')


