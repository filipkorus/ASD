import os

def main():
	board = [' ' for _ in range(9)]
	player = 'o'  # define who starts
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
		if winner == 'draw':
			print('It\'s a draw!')
		else:
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
			console_clear()
			print_board(board)
		if winner == 'draw':
			print('It\'s a draw!')
		else:
			print(f'{"You win!" if player == "x" else "AI wins!"}')

def console_clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_game_mode() -> int:
	print('-----MENU-----')
	print('Choose game mode: ')
	print('1) Player vs Player')
	print('2) Player vs AI')
	game_mode = int(input('Insert number:'))
	while game_mode < 1 or game_mode > 2:
		game_mode = int(input('Incorrect game mode! Try again:'))
	return game_mode

def print_board(board: list):
	for i in range(1, 10):
		if i % 3 == 1:
			print('-------------')
		print('|', board[i - 1], '', end='')
		if i % 3 == 0:
			print('|')
	print('-------------')

def check_win(board: list) -> str:
	for i in range(3):
		if board[3 * i] != ' ' and board[3 * i] == board[1 + 3 * i] == board[2 + 3 * i]:
			return board[3 * i]

	for i in range(3):
		if board[i] != ' ' and board[i] == board[3 + i] == board[6 + i]:
			return board[i]

	if board[0] != ' ' and board[0] == board[4] == board[8]:
		return board[0]

	if board[2] != ' ' and board[2] == board[4] == board[6]:
		return board[2]

	if ' ' not in board:
		return 'draw'

	return ' '  # no win yet

def is_position_correct(board: list, pos: int) -> bool:
	if pos < 0 or pos > 8:
		return False
	return board[pos] == ' '

def get_user_move(board: list, player: str) -> int:
	pos = int(input(f'Turn: {player}, insert place index (1-9):')) - 1
	while not is_position_correct(board, pos):
		pos = int(input(f'Incorrect place! Try again:'))
	return pos

def get_AI_move(board: list) -> int:
	best_score = -999
	move = 0
	for i in range(9):
		if is_position_correct(board, i):
			board[i] = 'x'
			score = minimax(board, 0, False)
			board[i] = ' '
			if score > best_score:
				best_score = score
				move = i
	return move

def minimax(board: list, depth: int, is_maximizing: bool) -> int:
	scores = {
		'x': 1,
		'o': -1,
		'draw': 0
	}
	result = check_win(board)
	if result != ' ':
		score = scores[result]
		return score

	best_score = (-999 if is_maximizing else 999)
	for i in range(9):
		if is_position_correct(board, i):
			board[i] = ('x' if is_maximizing else 'o')
			score = minimax(board, depth + 1, not is_maximizing)
			board[i] = ' '
			best_score = max(score, best_score) if is_maximizing else min(score, best_score)

	return best_score

if __name__ == '__main__':
	main()
