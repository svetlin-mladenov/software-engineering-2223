from enum import Enum

class WhiteFigures(Enum):
    Pawn = '♙'
    Rook = '♖'
    Knight = '♘'
    Bishop = '♗'
    King = '♔'
    Queen = '♕'

class BlackFigures(Enum):
    Pawn = '♟'
    Rook = '♜'
    Knight = '♞'
    Bishop = '♝'
    King = '♚'
    Queen = '♛'

class ChessBoard():
    
    def __init__(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        order_for_last_row = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        
        for i in range(8):
            self.board[1][i] = BlackFigures['Pawn'].value
            self.board[0][i] = BlackFigures[order_for_last_row[i]].value

            self.board[6][i] = WhiteFigures['Pawn'].value
            self.board[7][i] = WhiteFigures[order_for_last_row[i]].value

    def print_chess_board(self):
        print('┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓')
        
        for row in range(8):
            print('┃', end= '')
            
            for column in range(8):
                print(f'{self.board[row][column]}  ┃', end= '')
            print()
            
            if(row != 7):
                print('┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫')
                
        print('┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛')
            

chess_board = ChessBoard();
chess_board.print_chess_board()
