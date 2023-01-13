from dataclasses import dataclass
import termcolor as tc


@dataclass
class WhiteFigures:
    pawn = " ♙  "
    rook = ' ♖  '
    knight = ' ♘  '
    bishop = ' ♗  '
    king = ' ♔  '
    queen = ' ♕  '
    order_of_last_row = ['rook', 'knight', 'bishop',
                         'queen', 'king', 'bishop', 'knight', 'rook']


@dataclass
class BlackFigures:
    pawn = ' ♟  '
    rook = ' ♜  '
    knight = ' ♞  '
    bishop = ' ♝  '
    king = ' ♚  '
    queen = ' ♛  '
    order_of_last_row = ['rook', 'knight', 'bishop',
                         'queen', 'king', 'bishop', 'knight', 'rook']


class ChessBoard:
    def __init__(self) -> None:
        self.board = [[[] for i in range(8)] for j in range(8)]
        # order_of_last_row = ['rook', 'knight', 'bishop',
        #                     'queen', 'king', 'bishop', 'knight', 'rook']
        for i in range(0, 8):
            if i % 2 == 0:
                color = 0
            else:
                color = 1
            for j in range(0, 8):
                if color > 1:
                    color = 0

                self.board[i][j].append(color)
                color += 1

        self.board[0][0].append(BlackFigures.rook)
        self.board[0][1].append(BlackFigures.knight)
        self.board[0][2].append(BlackFigures.bishop)
        self.board[0][3].append(BlackFigures.queen)
        self.board[0][4].append(BlackFigures.king)
        self.board[0][5].append(BlackFigures.bishop)
        self.board[0][6].append(BlackFigures.knight)
        self.board[0][7].append(BlackFigures.rook)

        for i in range(0, 8):
            self.board[1][i].append(BlackFigures.pawn)

        for i in range(2, 6):
            for j in range(0, 8):
                self.board[i][j].append("    ")

        for i in range(0, 8):
            self.board[6][i].append(WhiteFigures.pawn)

        self.board[7][0].append(WhiteFigures.rook)
        self.board[7][1].append(WhiteFigures.knight)
        self.board[7][2].append(WhiteFigures.bishop)
        self.board[7][3].append(WhiteFigures.queen)
        self.board[7][4].append(WhiteFigures.king)
        self.board[7][5].append(WhiteFigures.bishop)
        self.board[7][6].append(WhiteFigures.knight)
        self.board[7][7].append(WhiteFigures.rook)

    def print_chess_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j][0] == 0:
                    tc.cprint(self.board[i][j][1], "grey", "on_white", end="")
                else:
                    tc.cprint(self.board[i][j][1], "grey", "on_grey", end="")
                if j == 7:
                    print("\n", end="")


if __name__ == "__main__":
    my_board = ChessBoard()
    my_board.print_chess_board()
