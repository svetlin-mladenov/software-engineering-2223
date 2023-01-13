from termcolor import *


class ChessPiece:
    def __init__(self, fen_letter: str) -> None:
        self.fen_letter = fen_letter
        if fen_letter.islower():
            self.color = "black"

        else:
            self.color = "white"

        self.symbol = ChessBoard.piece_symbols[fen_letter]

    def __str__(self) -> str:
        return self.symbol


class ChessBoard:
    FILE_LETTERS = "abcdefgh"
    piece_symbols = {
        "p": "♟ ",
        "n": "♞ ",
        "b": "♝ ",
        "r": "♜ ",
        "q": "♛ ",
        "k": "♚ ",
        "P": "♙ ",
        "N": "♘ ",
        "B": "♗ ",
        "R": "♖ ",
        "Q": "♕ ",
        "K": "♔ "
    }

    def __init__(self, fen_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") -> None:
        self.board = {file : [None for square in range(9)] for file in self.FILE_LETTERS}

        fen_ranks = fen_str.split(" ")[0].split("/")

        for rank_num, fen_rank in enumerate(fen_ranks, start = 1):
            curr_pos = 1
            for fen_letter in fen_rank:
                if fen_letter.isdigit():
                    curr_pos += int(fen_letter)
                    continue

                else:
                    self.board[chr(ord("`") + curr_pos)][rank_num] = ChessPiece(fen_letter)

                curr_pos += 1

    def print_position(self) -> None:
        for rank_num in range(1, 9):
            print(f"{rank_num} ", end="")
            for i, file_letter in enumerate(self.FILE_LETTERS, start = 1):
                piece = self.board[file_letter][rank_num]
                if (rank_num % 2 == 0 and i % 2 == 0) or (rank_num % 2 != 0 and i % 2 != 0):
                    cprint(piece or "  ", attrs=["reverse"], end="")
                else:
                    print(piece or "  ", end="")

            print("")

        print("  ", end="")
        for file_letter in self.FILE_LETTERS:
            print(f"{file_letter} ", end="")

        print("")


def main() -> None:

    chess_board = ChessBoard("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
    chess_board.print_position()


if __name__ == "__main__":
    main()