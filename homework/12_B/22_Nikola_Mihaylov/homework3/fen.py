from termcolor import cprint

class ChessPosition:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def start(self, fen):
        rows = fen.split()[0].split('/')
        for rank, row in enumerate(rows):
            file = 0
            for char in row:
                if char.isdigit():
                    file += int(char)
                else:
                    piece = {
                        'p': "♟",
                        'n': "♞",
                        'b': "♝",
                        'r': "♜",
                        'q': "♛",
                        'k': "♚",
                        'P': "♙",
                        'N': "♘",
                        'B': "♗",
                        'R': "♖",
                        'Q': "♕",
                        'K': "♔"
                    }
                    self.board[rank][file] = piece.get(char)
                    file += 1

    def print(self):
        for x in range(8):
            for y in range(8):
                print(self.board[x][y], end = "") if (x + y) % 2 else cprint(self.board[x][y], "grey", "on_white", end = "")
            print()

che_p = ChessPosition()
che_p.start("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
che_p.print()
