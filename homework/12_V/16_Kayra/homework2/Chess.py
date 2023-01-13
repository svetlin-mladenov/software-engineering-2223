import termcolor as tc

class chess:
    def __init__(self):
        self.board = [
            ["\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"],
            ["\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659"],
            ["\u2656","\u2658","\u2657","\u2655","\u2654","\u2657","\u2658","\u2656"]
        ]
    def print_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 != 0:
                    tc.cprint(self.board[i][j], 'white', 'on_grey', end=' ')
                else:
                    tc.cprint(self.board[i][j], 'white', 'on_yellow', end=' ')
            print()


chess = chess()
chess.print_board()

