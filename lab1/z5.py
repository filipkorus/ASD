from random import randint

def main():
	board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	player = 'o'
	winner = ' '
	game_mode = get_game_mode()
	if game_mode == 1:
		print('Game mode: P v P')
		print_board(board)
		while winner == ' ':
			row, place = get_move(board, player)
			board[row][place] = player
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
				row, place = get_AI_move(board)
			else:
				row, place = get_move(board, player)
			board[row][place] = player
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
	for row in range(3):
		print('-------------')
		print('| ', end='')
		for place in range(3):
			print(board[row][place], '| ', end='')
			if place == 2:
				print('')

	print('-------------')

def get_move(board, player):
	pos = int(input(f'Turn: {player}, insert place index (1-9):'))
	while is_position_taken(board, pos):
		pos = input(f'Place was already taken! Try again:')

	return format_position(pos)

def get_AI_move(board):
	pos = randint(1, 9)

	while is_position_taken(board, pos):
		pos = randint(1, 9)

	return format_position(pos)

def check_win(board):
	for row in range(3):
		if board[row][0] != ' ' and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
			return board[row][0]

	for col in range(3):
		if board[0][col] != ' ' and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
			return board[0][col]

	if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[0][0]

	if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[0][0]

	return ' '  # no win yet

def format_position(pos):
	place = (pos % 3) - 1
	row = 0
	if 4 <= pos <= 6:
		row = 1
	elif 7 <= pos <= 9:
		row = 2

	return row, place

def is_position_taken(board, pos):
	row, place = format_position(pos)
	return board[row][place] != ' '

if __name__ == '__main__':
	main()
