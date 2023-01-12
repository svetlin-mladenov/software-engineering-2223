from termcolor import colored, cprint


class FenChess:
    figure_dict = {
        "p": "♟",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "P": "♙",
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔"
    }

    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.chess_board = []
        for _ in range(8):
            self.chess_board.append([])

        fen_board = fen.split(" ")[0]

        index = 0

        for row in fen_board.split("/"):
            column = 0
            for symbol in row:
                if symbol.isdigit():
                    for _ in range(int(symbol)):
                        self.chess_board[index].append(
                            [(index + column) % 2, "   "])
                        column += 1
                else:
                    self.chess_board[index].append(
                        [(index + column) % 2, f" {self.figure_dict[symbol]} "])
                    column += 1
            index += 1

    def print_chess_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.chess_board[i][j][0] == 0:
                    cprint(
                        self.chess_board[i][j][1], "grey", "on_white", end="")
                else:
                    cprint(
                        self.chess_board[i][j][1], "grey", "on_grey", end="")
                if j == 7:
                    print("\n", end="")


if __name__ == "__main__":
    my_board = FenChess(
        "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
    my_board.print_chess_board()
