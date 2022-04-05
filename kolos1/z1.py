import math
import random

class LOTTO:
	def __init__(self, list_size: int) -> None:
		if not 5 <= list_size <= 6:
			raise ValueError('list_size must be between 5 and 6')
		self.L = [random.randint(0, 48) for _ in range(list_size)]

	def __str__(self) -> str:
		return str(self.L)

	def SPRAWDZ(self, L2) -> bool:
		return False if len(self.L) != len(L2.L) else sorted(self.L) == sorted(L2.L)

	def GRAJ(self) -> float:
		return 1/math.comb(49, len(self.L))

def save_to_file(L1: LOTTO, L2: LOTTO) -> None:
	print(
		f'L1: {L1}',
		f'L2: {L2}',
		f'SPRAWDZ: {L1.SPRAWDZ(L2)}',
		f'GRAJ: {L1.GRAJ()}',
		sep='\n',
		file=open(f'{L1.L[0]}{L1.L[1]}.txt', 'w', encoding='utf-8')
	)

if __name__ == '__main__':
	L1 = LOTTO(5)
	L2 = LOTTO(6)

	save_to_file(L1, L2)
