if __name__ == '__main__':
	f = open('zadanie2.csv', 'r')

	items = []
	index = 1
	for line in f:  # insert every line from file to 'items' array as a dict
		val = line.split(',', 1)[1].replace('\n', '').lower()
		if val != '' and val != 'val':
			items.append({'id': index, 'val': val})
			index += 1

	for i, item in enumerate(items):
		deleted_words = []
		for word in item['val'].split(' '):
			word = word.strip(',.')  # delete commas and dots from word
			if len(word) > 1 and abs(ord(word[0]) - ord(word[1])) == 1:  # check if first two chars are next to each other in ASCII
				items[i]['val'].replace(word, '')  # delete word from string
				deleted_words.append(word)
		if len(deleted_words):
			print(f"id: {item['id']}, deleted words: {deleted_words}")
