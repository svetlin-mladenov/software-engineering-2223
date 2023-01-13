class ChessBoard():

    def __init__(self):
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


chess_board = ChessBoard();
chess_board.print_chess_board()
