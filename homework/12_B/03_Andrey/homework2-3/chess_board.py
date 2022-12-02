import termcolor
from chess_pieces import *


class ChessBoard():

    def __init__(this):
        this.clear()
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(len(figures)):
            this.board[0][i] = figures[i].get_black()
            this.board[7][i] = figures[i].get_white()
        for i in range(8):
            this.board[1][i] = Pawn.get_black()
            this.board[6][i] = Pawn.get_white()

        this.FEN_notations = {"P" : Pawn , "R" : Rook , "N" : Knight , "B" : Bishop , "Q" : Queen , "K" : King}

    def clear(this):
        this.board = [[ChessPiece(" ") for j in range(8) ] for i in range(8)]


    def input_FEN_state(this, fenstring):
        this.clear()
        row = 0
        column = 0
        FEN_keys = this.FEN_notations.keys()
        for char in fenstring:

            if char.upper() in FEN_keys:
                if char.upper() == char:
                    this.board[row][column] = this.FEN_notations[char].get_white()
                else:
                    this.board[row][column] = this.FEN_notations[char.upper()].get_black()
                column += 1
            elif char == "/":
                row += 1
            elif char == " ":
                break
            else:
                column += int(char)

            if row > 7:
                row -= 8
            if column > 7:
                column -= 8

        
   
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
Chess.input_FEN_state("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
print ("After applying FEN notation: ")
Chess.print()
