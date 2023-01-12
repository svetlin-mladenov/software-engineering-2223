from termcolor import colored, cprint

class chess_piece:
	def __init__(self, horizontal_position, vertical_position, color, piece):
		self.horizontal_position = horizontal_position
		self.vertical_position = vertical_position
		self.color = color
		self.piece = piece

def fen_parser(fen):
	pieces = []

	for i in fen:
		if i == " ":
			break

		elif i == "/":
			continue

		elif i.isdigit():
			for j in range(int(i)):
				pieces.append(chess_piece(j, len(pieces) // 8, "white", " "))

		elif i.isupper():
			pieces.append(chess_piece(len(pieces) % 8, len(pieces) // 8, "white", i))

		elif i.islower():
			pieces.append(chess_piece(len(pieces) % 8, len(pieces) // 8, "black", i))

	return pieces


def print_board(fen):
	board = [None] * 8

	for i in range(8):
		board[i] = [None] * 8

	pieces = fen_parser(fen)

	for i in pieces:
		board[i.horizontal_position][i.vertical_position] = i

	for i in range(8):
		for j in range(8):
			if board[i][j] == None:
				print(end=" ")

			elif board[i][j].color == "white":
				text = colored(board[i][j].piece, "white")
				cprint(text, end=" ")

			else:
				text = colored(board[i][j].piece, "grey", "on_white")
				cprint(text, end=" ")
		print()

print_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print_board("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
