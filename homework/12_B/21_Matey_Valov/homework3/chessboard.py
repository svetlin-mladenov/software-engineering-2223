from enum import Enum
from termcolor import cprint
from colorama import init

init(autoreset=True)

Pieces = {
    'R' : '♖ ',
    'N' : '♘ ',
    'B' : '♗ ',
    'Q' : '♕ ',
    'K' : '♔ ',
    'P' : '♙ ',
    'r' : '♜ ',
    'n' : '♞ ',
    'b' : '♝ ',
    'q' : '♛ ',
    'k' : '♚ ',
    'p' : '♟ '
}

class Board():  
    def __init__(self):
        self.board = [['  ' for i in range(8)] for j in range(8)]
    
    def FenParse(self, string):
        row = 0
        column = 0
        
        i = 0
        while(string[i] != ' '):
            if(string[i].isnumeric()):
                column += int(string[i])
                i += 1
            
            elif(string[i] == '/'):
                row += 1;
                column = 0
                i += 1
                
            else:
                slot = Pieces[string[i]]
                self.board[row][column] = slot
                column += 1
                i += 1
            
            
    def PrintBoard(self):
        BGcolor = 'white'
        
        for i in range(8):
            print(f"{8-i} ", end="")

            for j in range(8):
                if BGcolor == 'black':
                    print(f"{self.board[i][j]}", end="")
                    BGcolor = 'white'
                else:
                    cprint(f"{self.board[i][j]}", None, 'on_white', end="")
                    BGcolor = 'black'
            print()
            
            if(BGcolor == 'black'):
                BGcolor = 'white'
            else:
                BGcolor = 'black'
        
        print("  A B C D E F G H ")
 
        
ChessBoard = Board()
ChessBoard.FenParse("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K w - - 0 25")
ChessBoard.PrintBoard()