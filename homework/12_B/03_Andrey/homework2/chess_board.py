import termcolor
from chess_pieces import *


class ChessBoard():

    def __init__(this):
        this.board = [[ChessPiece(" ") for j in range(8) ] for i in range(8)]
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(len(figures)):
            this.board[0][i] = figures[i].get_black()
            this.board[7][i] = figures[i].get_white()
        for i in range(8):
            this.board[1][i] = Pawn.get_black()
            this.board[6][i] = Pawn.get_white()


    def print(this):

        print("  ┏━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┓")
        for i in range(8):
            print(f"{8-i} ┃ ", end="")

            for j in range(8):
                print(f"{this.board[i][j].symbol}  ┃ ", end="")

            if i !=7 :
                print("\n  ┣━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━┫")

        print("\n  ┗━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┛")
        print("     A    B    C    D    E    F    G    H")


Chess = ChessBoard()
Chess.print()
