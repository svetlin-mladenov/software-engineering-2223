from termcolor import colored


class Figures:
    def __init__(self, color):
        self.color = color
        self.fig = {
            'C': 2,
            'H': 2,
            'B': 2,
            'Q': 1,
            'K': 1,
            'P': 8
        }

class Board:
    def __init__(self):
        self.size = 8
        self.board = [[] for _ in range(8)]
        self.white_team = Figures('white')
        self.black_team = Figures('black')
    
    def createBoard(self):
        for c in range (8):
            for r in range (8):
                if c % 2 == r % 2:
                    self.board[c].append(colored(" * ", "grey", "on_white"))
                else: 
                    self.board[c].append(" * ")

        # for keyW, valueW in self.whiteTeam.fig.items():
        #     if valueW == 2:
        #         if keyW == 'C':
        #             self.board[0][0] = colored(" ♖ ", "grey", "on_white")
        #             self.board[0][self.size - 1] = " ♜ "
        #         elif keyW == 'H':
        #             self.board[0][1] = " ♞ "
        #             self.board[0][self.size - 2] = colored(" ♘ ", "grey", "on_white")
        #         elif keyW == 'B':
        #             self.board[0][2] = colored(" ♗ ", "grey", "on_white")
        #             self.board[0][self.size - 3] = " ♝ "
        #     elif valueW == 1:
        #         if keyW == 'Q':
        #             self.board[0][3] = " ♛ "
        #         else:
        #             self.board[0][4] = colored(" ♔ ", "grey", "on_white")
        #     else:
        #         for k in range(valueW):
        #             if k % 2 == 1:
        #                 self.board[1][k] = colored(" ♙ ", "grey", "on_white")
        #             else:
        #                 self.board[1][k] = " ♟ "

        # for keyB, valueB in self.blackTeam.fig.items():
        #     if valueB == 2:
        #         if keyB == 'C':
        #             self.board[7][0] = " ♖ "
        #             self.board[7][self.size - 1] = colored(" ♜ ", "grey", "on_white")
        #         elif keyB == 'H':
        #             self.board[7][1] = colored(" ♞ ", "grey", "on_white")
        #             self.board[7][self.size - 2] = " ♘ "
        #         elif keyB == 'B':
        #             self.board[7][2] = " ♗ "
        #             self.board[7][self.size - 3] = colored(" ♝ ", "grey", "on_white")
        #     elif valueB == 1:
        #         if keyB == 'Q':
        #             self.board[7][3] = colored(" ♛ ", "grey", "on_white")
        #         else:
        #             self.board[7][4] = " ♔ "
        #     else:
        #         for l in range(valueB):
        #             if l % 2 == 0:
        #                 self.board[6][l] = colored(" ♟ ", "grey", "on_white")
        #             else:
        #                 self.board[6][l] = " ♙ "

    def printBoard(self):
        for i in self.board:
            for j in i:
                print (j, end=" ")
            print('\n')

    def setPossitions(self, fen):
        rows = fen.split('/')
        i = 0
        for row in rows:
            j = 0
            for symbol in row:
                if symbol == 'r' :
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♜ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♖ "
                elif symbol == 'R':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♖ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♜ "
                elif symbol == 'n' :
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♞ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♘ "
                elif symbol == 'N':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♘ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♞ "
                elif symbol == 'b' :
                    if (j <= 7):
                        if i % 2 == j % 2:
                            self.board[i][j] = (colored(" ♝ ", "grey", "on_white"))
                        else:
                            self.board[i][j] = " ♗ "
                elif symbol == 'B':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♗ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♝ "
                elif symbol == 'q' :
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♛ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♕ "
                elif symbol == 'Q':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♕ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♛ "
                elif symbol == 'k' :
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♚ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♔ "
                elif symbol == 'K':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♔ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♚ "
                elif symbol == 'p' :
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♟ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♙ "
                elif symbol == 'P':
                    if i % 2 == j % 2:
                        self.board[i][j] = (colored(" ♙ ", "grey", "on_white"))
                    else:
                        self.board[i][j] = " ♟ "
                elif symbol == '2':
                    j += 1
                elif symbol == '3':
                    j += 2
                elif symbol == '4':
                    j += 3
                elif symbol == '5':
                    j += 4
                elif symbol == '6':
                    j += 5
                elif symbol == '7':
                    j += 6
                elif symbol == '8':
                    j += 7
                j += 1
            i += 1

board = Board()
board.createBoard()
#fen = input("Enter FEN: ")
fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
board.setPossitions(fen)
print("- - - - - CHESS BOARD - - - - -\n")
board.printBoard()