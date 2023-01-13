from piece import setup_chess_pieces

class Chessboard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        
        red_pieces = setup_chess_pieces("red")
        blue_pieces = setup_chess_pieces("blue")
            
        # populate board with pieces
        for i in range(8):
            self.board[1][i] = red_pieces[i]
            self.board[6][i] = blue_pieces[i]

        for i in range(8, 16):
            self.board[0][i-8] = red_pieces[i]
            self.board[7][i-8] = blue_pieces[i]
    
    def clear_board(self):
        """
        Clears the chessboard by setting all squares to None
        """
        for i in range(8):
            for j in range(8):
                self.board[i][j] = None

    def print_board(self):
        buffer = str()
        for i in range(17):
            buffer += "- "
        print(buffer)       

        for row in range(len(self.board)):
            res = "|"
            for col in self.board[row]:
                if col is None:
                    res += "   |"
                else:
                    res += (" " + str(col.name) + " |")
            
        
            print(res)
            print(buffer)