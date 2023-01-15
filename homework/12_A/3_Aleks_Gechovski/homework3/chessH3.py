from termcolor import *

class GameBoard:
    RANK_LETTERS = "abcdefgh"
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
        # The board is a dictionary of lists, meaning that a piece can be accessed like:
        #   board["a"][1]
        #   board["e"][3]
        #   and so on ...
        self.board = {rank : [None for square in range(9)] for rank in self.RANK_LETTERS}

        fen_files = fen_str.split(" ")[0].split("/")

        # Fill the board with the pieces specified in the FEN string
        for file_num, fen_file in enumerate(fen_files, start = 1):
            curr_pos = 1
            for fen_letter in fen_file:
                if fen_letter.isdigit():
                    curr_pos += int(fen_letter)
                    continue

                else:
                    self.board[chr(ord("`") + curr_pos)][file_num] = GamePiece(fen_letter)

                curr_pos += 1

    def display_position(self) -> None:
        """ Print the current game position """
        for file_num in range(1, 9):
            print(f"{file_num} ", end="")
            for i, rank_letter in enumerate(self.RANK_LETTERS, start = 1):
                piece = self.board[rank_letter][file_num]
                if (file_num % 2 == 0 and i % 2 == 0) or (file_num % 2 != 0 and i % 2 != 0):
                    cprint(piece or "  ", attrs=["reverse"], end="")

                else:
                    print(piece or "  ", end="")

            print("")

        print("  ", end="")
        for file_letter in self.RANK_LETTERS:
            print(f"{file_letter} ", end="")

        print("")

class GamePiece:

    def __init__(self, fen_letter: str) -> None:
        self.fen_letter = fen_letter
        if fen_letter.islower():
            self.color = "black"

        else:
            self.color = "white"

        self.symbol = GameBoard.piece_symbols[fen_letter]

    def __str__(self) -> str:
        return self.symbol


def main() -> None:

    chess_board = GameBoard("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
    chess_board.display_position()


if __name__ == "__main__":
    main()