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
        
        self.FEN_symbols = {'P' : 'Pawn' , 'R' : 'Rook' , 'N' : 'Knight' , 'B' : 'Bishop' , 'Q' : 'Queen' , "K" : 'King'}

    def clear_chess_board(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]

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
        
    def make_fen(self, fen_string):
        self.clear_chess_board()
        column = 0
        row = 0
        fen_symbols_keys = self.FEN_symbols.keys()
    
        for symbol in fen_string:
            if symbol is ' ':
                break
            
            elif symbol.upper() in fen_symbols_keys:
                if symbol.isupper():
                    self.board[row][column] = WhiteFigures[self.FEN_symbols[symbol.upper()]].value
                else:
                    self.board[row][column] = BlackFigures[self.FEN_symbols[symbol.upper()]].value

                column += 1
            elif symbol is '/':
                row += 1
        
            else:
                column += int(symbol)
            
            if row > 7:
                row = 0
                
            if column > 7:
                column = 0

chess_board = ChessBoard();
chess_board.print_chess_board()
chess_board.make_fen('r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25');
chess_board.print_chess_board()
