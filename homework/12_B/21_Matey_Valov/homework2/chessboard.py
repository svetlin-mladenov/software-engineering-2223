from enum import Enum
from termcolor import cprint
from colorama import init

init(autoreset=True)

class Whites(Enum):
    Rook = '♖'
    Knight = '♘'
    Bishop = '♗'
    Queen = '♕'
    King = '♔'
    Pawn = '♙'
    
class Blacks(Enum):
    Rook = '♜'
    Knight = '♞'
    Bishop = '♝'
    Queen = '♛'
    King = '♚'
    Pawn = '♟'


class Board():
    board = [[' ' for i in range(8)] for j in range(8)]
    
    def __init__(this):
        order = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for i in range(8):
            this.board[0][i] = Blacks[order[i]].value
            this.board[7][i] = Whites[order[i]].value
            
            this.board[1][i] = Blacks['Pawn'].value
            this.board[6][i] = Whites['Pawn'].value
         
            
    def PrintBoard(this):
        BGcolor = 'white'
        
        for i in range(8):
            print(f"{8-i} ", end="")

            for j in range(8):
                if BGcolor == 'black':
                    print(f"{this.board[i][j]}", end="")
                    BGcolor = 'white'
                else:
                    cprint(f"{this.board[i][j]}", None, 'on_white', end="")
                    BGcolor = 'black'
            print()
            
            if(BGcolor == 'black'):
                BGcolor = 'white'
            else:
                BGcolor = 'black'
        
        print("  ABCDEFGH")
 
        
ChessBoard = Board()
ChessBoard.PrintBoard()