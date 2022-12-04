from figures import * 
from termcolor import *

board = [[None for i in range(8)] for j in range(8)]


# Structure of Black Pieces and then for cycle for placing them on board
BlackPieces = [Rook("black").symbol,Knight("black").symbol,Bishop("black").symbol,Queen("black").symbol,King("black").symbol,Bishop("black").symbol,Knight("black").symbol,Rook("black").symbol]

for i in range(8):
    board[0][i] = BlackPieces[i]
    board[1][i] = Pawn("black").symbol

# Structure of White Pieces and then for cycle for placing them on board
WhitePieces = [Rook("white").symbol,Knight("white").symbol,Bishop("white").symbol,Queen("white").symbol,King("white").symbol,Bishop("white").symbol,Knight("white").symbol,Rook("white").symbol]

for i in range(8):
    board[7][i] = WhitePieces[i]
    board[6][i] = Pawn("white").symbol

chess_row = 8
for i,row in enumerate(board):
    print()
    print(chess_row,end=" ")
    for pos,j in enumerate(row):
        if i % 2 == 0:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  " , 'yellow', attrs=['reverse'],end = "")
            else:
                cprint(j or "  " , 'white', attrs=['reverse'],end = "")
        else:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  " , 'white', attrs=['reverse'],end = "")
            else:
                cprint(j or "  " , 'yellow', attrs=['reverse'],end = "")
    if i == 7:
        print()
        print(' ','a','b','c','d','e','f','g','h', sep=" ")
    chess_row -= 1
