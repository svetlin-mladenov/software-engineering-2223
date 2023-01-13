from dataclasses import dataclass
import termcolor

@dataclass
class BlackFigures:
    pawn = ' ♟  '
    rook = ' ♜  '
    knight = ' ♞  '
    bishop = ' ♝  '
    king = ' ♚  '
    queen = ' ♛  '

@dataclass
class WhiteFigures:
    pawn = " ♙  "
    rook = ' ♖  '
    knight = ' ♘  '
    bishop = ' ♗  '
    king = ' ♔  '
    queen = ' ♕  '


class ChessBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = [[[] for _ in range(self.width)] for _ in range(self.height)]

        self.color_board()
        self.populate_figures()

    def color_board(self):
        for i in range(0, self.height):
            inital_color = (1 if i % 2 else 0) 
            color = inital_color
     
            for j in range(0, self.width):

                self.board[i][j].append(color)

                color = (inital_color if j % 2 else (1 if inital_color == 0 else 0)) 

    def populate_figures(self):
        def populate_white():
            white_order = [WhiteFigures.rook, WhiteFigures.knight, WhiteFigures.bishop, WhiteFigures.queen, WhiteFigures.king, WhiteFigures.bishop, WhiteFigures.knight, WhiteFigures.rook]

            for i in range(self.width):
                if i > 7:
                    self.board[self.height - 1][i].append("    ")
                    self.board[self.height - 2][i].append("    ")
                    continue
                self.board[self.height - 1][i].append(white_order[i])
                self.board[self.height - 2][i].append(WhiteFigures.pawn)
        
        def populate_black():
            black_order = [BlackFigures.rook, BlackFigures.knight, BlackFigures.bishop, BlackFigures.queen, BlackFigures.king, BlackFigures.bishop, BlackFigures.knight, BlackFigures.rook]

            for i in range(self.width):
                if i > 7:
                    self.board[0][i].append("    ")
                    self.board[1][i].append("    ")
                    continue
                self.board[0][i].append(black_order[i])
                self.board[1][i].append(BlackFigures.pawn)

        populate_black()

        for i in range(2, self.height - 2):
            for j in range(0, self.width):
                self.board[i][j].append("    ")

        populate_white()

    def print_board(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j][0] == 0:
                    termcolor.cprint(self.board[i][j][1], "grey", "on_white", end="")
                else:
                    termcolor.cprint(self.board[i][j][1], "grey", "on_grey", end="")
                if j == self.width - 1:
                    print("\n", end="")


test_board = ChessBoard(8, 8)

test_board.print_board()