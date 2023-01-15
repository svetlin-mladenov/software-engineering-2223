from enum import IntEnum, StrEnum
from termcolor import cprint

class Piece:
	type = None
	color = None

	def __init__(self, pieceType, pieceColor):
		if isinstance(pieceType, int):
			if pieceType not in range(0, 7):
				raise ValueError("Type not in range [0; 6]")
			self.type = pieceType

		elif isinstance(pieceType, str):
			self.type = Piece.Type[pieceType]

		else:
			raise TypeError("Type must be int or str (preferred: use Piece.Type enum)")

		if isinstance(pieceColor, int):
			if pieceColor not in range(0, 3):
				raise ValueError("Color not in range [0; 2]")
			self.color = pieceColor

		elif isinstance(pieceColor, str):
			self.color = Piece.Color[pieceColor]

		else:
			raise TypeError("Color must be int or str (preferred: use Piece.Color enum)")

	def __str__(self) -> str:
		# imo the black pieces look better on cygwin for some reason so I'm using those
		# return Piece.PIECES[self.color][self.type]
		return Piece.BLACK_PIECES[self.type]

	PIECES = [["   ", "   ", "   ", "   ", "   ", "   ", "   "],
			  ["   ", " ♙ ", " ♗ ", " ♘ ", " ♖ ", " ♕ ", " ♔ "],
			  ["   ", " ♟ ", " ♝ ", " ♞ ", " ♜ ", " ♛ ", " ♚ "]]

	WHITE_PIECES = ["   ", " ♙ ", " ♗ ", " ♘ ", " ♖ ", " ♕ ", " ♔ "]
	BLACK_PIECES = ["   ", " ♟ ", " ♝ ", " ♞ ", " ♜ ", " ♛ ", " ♚ "]

	class Color(IntEnum):
		NONE = 0
		WHITE = 1
		BLACK = 2

	class Type(IntEnum):
		NONE = 0
		PAWN = 1
		BISHOP = 2
		KNIGHT = 3
		ROOK = 4
		QUEEN = 5
		KING = 6

	# Do I need this? probably not. oh well.
	# Horizontal position
	class File(IntEnum):
		A = 0
		B = 1
		C = 2
		D = 3
		E = 4
		F = 5
		G = 6
		H = 7

	# Vertical position
	class Rank(IntEnum):
		EIGHTH = 0
		SEVENTH = 1
		SIXTH = 2
		FIFTH = 3
		FOURTH = 4
		THIRD = 5
		SECOND = 6
		FIRST = 7

class Board:
	pieces = None

	def __init__(self, *, empty = False):
		self.pieces = [[Piece(Piece.Type.NONE, Piece.Color.NONE)] * 8 for i in range(8)]

		if not empty:
			for i in range(0, 8):
				self.pieces[i][Piece.Rank.SECOND] = Piece(Piece.Type.PAWN, Piece.Color.WHITE)
				self.pieces[i][Piece.Rank.SEVENTH] = Piece(Piece.Type.PAWN, Piece.Color.BLACK)

			for i in range(0, 8):
				pieceType = 0
				if i == 0 or i == 7:
					pieceType = Piece.Type.ROOK
				elif i == 1 or i == 6:
					pieceType = Piece.Type.BISHOP
				elif i == 2 or i == 5:
					pieceType = Piece.Type.KNIGHT
				elif i == 3:
					pieceType = Piece.Type.QUEEN
				elif i == 4:
					pieceType = Piece.Type.KING

				self.pieces[i][Piece.Rank.FIRST] = Piece(pieceType, Piece.Color.WHITE)
				self.pieces[i][Piece.Rank.EIGHTH] = Piece(pieceType, Piece.Color.BLACK)

	def print_board(self):
		print("    A  B  C  D  E  F  G  H ")
		for y in range(0, 8):
			print(f" {8 - y} ", end = "")
			for x in range(0, 8):
				background = "on_cyan"
				if (x + y) % 2 == 0:
					background = "on_light_cyan"

				color = "black"
				if self.pieces[x][y].color == Piece.Color.WHITE:
					color = "white"

				cprint(str(self.pieces[x][y]), color, background, end = "")
			print(f" {8 - y} ")
		print("    A  B  C  D  E  F  G  H ")

	def set_FEN_position(self, position: str):
		position = position.strip()
		position = position[:position.find(" ")]
		for i in range (1, 9):
			position = position.replace(str(i), " " * i)
		position = position.split("/", 7)
		newBoard = Board(empty = True)

		for y in range(0, 8):
			for x in range(0, 8):
				pieceType = None
				pieceColor = None
				match position[y][x]:
					case "P":
						pieceType = Piece.Type.PAWN
						pieceColor = Piece.Color.WHITE
					case "p":
						pieceType = Piece.Type.PAWN
						pieceColor = Piece.Color.BLACK
					case "B":
						pieceType = Piece.Type.BISHOP
						pieceColor = Piece.Color.WHITE
					case "b":
						pieceType = Piece.Type.BISHOP
						pieceColor = Piece.Color.BLACK
					case "N":
						pieceType = Piece.Type.KNIGHT
						pieceColor = Piece.Color.WHITE
					case "n":
						pieceType = Piece.Type.KNIGHT
						pieceColor = Piece.Color.BLACK
					case "R":
						pieceType = Piece.Type.ROOK
						pieceColor = Piece.Color.WHITE
					case "r":
						pieceType = Piece.Type.ROOK
						pieceColor = Piece.Color.BLACK
					case "Q":
						pieceType = Piece.Type.QUEEN
						pieceColor = Piece.Color.WHITE
					case "q":
						pieceType = Piece.Type.QUEEN
						pieceColor = Piece.Color.BLACK
					case "K":
						pieceType = Piece.Type.KING
						pieceColor = Piece.Color.WHITE
					case "k":
						pieceType = Piece.Type.KING
						pieceColor = Piece.Color.BLACK
					case _:
						pieceType = Piece.Type.NONE
						pieceColor = Piece.Color.NONE

				newBoard.pieces[x][y] = Piece(pieceType, pieceColor)

		self.pieces = newBoard.pieces


board = Board(empty = True)
board.set_FEN_position("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
board.print_board()
