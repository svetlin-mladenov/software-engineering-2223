from termcolor import cprint

class Chess:
    def __init__(self) -> None:
        self.all_pieces = [["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"], 
                           ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"], 
                           [" ", " ", " ", " ", " ", " ", " ", " ", " "], 
                           [" ", " ", " ", " ", " ", " ", " ", " ", " "], 
                           [" ", " ", " ", " ", " ", " ", " ", " ", " "], 
                           [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                           ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"], 
                           ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]]
    
    def print_pos(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    cprint(self.all_pieces[i][j] + " ", 'white', 'on_grey', end='')
                else:
                    cprint(self.all_pieces[i][j] + " ", 'white', 'on_white', end='')
            print()
    

test = Chess()
test.print_pos()
