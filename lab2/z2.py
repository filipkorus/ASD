if __name__ == '__main__':
	f = open('zadanie2.csv', 'r')

	items = []
	for line in f:
		try:
			id = int(line.split(',')[0])
		except ValueError:
			id = 0
		val = line.split(',', 1)[1].replace('\n', '').lower()
		if val != '' and id != 0:
			items.append({
				'id': id,
				'val': val
			})
	items = sorted(items, key=lambda d: d['id'])

	for i in range(len(items) - 1):
		if items[i]['id'] == items[i + 1]['id']:
			items[i + 1]['id'] += 1

	for i, item in enumerate(items):
		deleted_words = []
		for word in item['val'].split(' '):
			if len(word) > 1 and abs(ord(word[0]) - ord(word[1])) == 1:
				items[i]['val'].replace(word, '')
				deleted_words.append(word)
		if len(deleted_words):
			print(f"id: {item['id']}, deleted words: {deleted_words}")
