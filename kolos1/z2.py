class CZYTELNIK:
	def __init__(self):
		self.lines = None

	def OTWORZ(self):
		self.file = open('lorem16.txt', 'r', encoding='utf-8')
		return self

	def CZYTAM(self):
		self.lines = self.file.readlines()
		del self.lines[1::2]  # delete even lines
		return self

	def SZUKAM(self, letter):
		counter = 0
		for line in self.lines:
			counter += line.count(letter)
		return counter

	def ZAMYKAM(self):
		self.file.close()
		return self

	def get_most_freq_letter(self):
		counter = {}
		char = ord('a')
		while char <= ord('z'):
			counter[chr(char)] = self.SZUKAM(chr(char))
			char += 1
		max_amount = 0
		max_amount_letter = ' '
		for letter, amount in counter.items():
			if max_amount < amount:
				max_amount = amount
				max_amount_letter = letter
		return max_amount_letter, max_amount

if __name__ == '__main__':
	c = CZYTELNIK()
	print(
		c.OTWORZ().CZYTAM().ZAMYKAM().get_most_freq_letter()
	)
