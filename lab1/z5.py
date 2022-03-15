from random import randint

def main():
	board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
	player = 'o'
	winner = ' '
	game_mode = get_game_mode()
	if game_mode == 1:
		print('Game mode: P v P')
		print_board(board)
		while winner == ' ':
			place = get_user_move(board, player)
			board[place] = player
			winner = check_win(board)
			player = ('o' if player == 'x' else 'x')
			print_board(board)
		print(f'Winner: {winner}')
	elif game_mode == 2:
		#  AI is always 'x' player
		print('Game mode: P v AI')
		print_board(board)
		while winner == ' ':
			if player == 'x':
				place = get_AI_move(board)
			else:
				place = get_user_move(board, player)
			board[place] = player
			winner = check_win(board)
			player = ('o' if player == 'x' else 'x')
			print_board(board)
		print(f'{"You win!" if player == "x" else "AI wins!"}')

def get_game_mode():
	print('-----MENU-----')
	print('Choose game mode: ')
	print('1) Player vs Player')
	print('2) Player vs AI')
	game_mode = int(input('Insert number:'))
	while game_mode < 1 or game_mode > 2:
		game_mode = int(input('Incorrect game mode! Try again:'))
	return game_mode

def print_board(board):
	for i in range(1, 10):
		if i % 3 == 1:
			print('-------------')
		print('|', board[i], '', end='')
		if i % 3 == 0:
			print('|')
	print('-------------')

def get_user_move(board, player):
	pos = int(input(f'Turn: {player}, insert place index (1-9):'))
	while is_position_correct(board, pos):
		pos = int(input(f'Incorrect place! Try again:'))
	return pos

def get_AI_move(board):
	pos = randint(1, 9)
	while is_position_correct(board, pos):
		pos = randint(1, 9)
	return pos

def check_win(board):
	for i in range(3):
		if board[1 + 3 * i] != ' ' and board[1 + 3 * i] == board[2 + 3 * i] == board[3 + 3 * i]:
			return board[1 + 3 * i]

	for i in range(3):
		if board[1 + i] != ' ' and board[1 + i] == board[4 + i] == board[7 + i]:
			return board[1 + i]

	if board[1] != ' ' and board[1] == board[5] and board[5] == board[9]:
		return board[1]

	if board[3] != ' ' and board[3] == board[5] and board[5] == board[7]:
		return board[3]

	return ' '  # no win yet

def is_position_correct(board, pos: int):
	if pos < 1 or pos > 9:
		return True
	return board[pos] != ' '

if __name__ == '__main__':
	main()
