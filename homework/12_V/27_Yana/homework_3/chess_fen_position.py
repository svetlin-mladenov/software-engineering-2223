from termcolor import cprint

class Chess:
    def __init__(self, fen: str) -> None:
        for ch in range(len(fen)):
            if fen[ch].lower():
                if fen[ch] == "r":
                    fen = fen.replace(fen[ch], "♖")
                if fen[ch] == "p":
                    fen = fen.replace(fen[ch], "♙")
                if fen[ch] == "b":
                    fen = fen.replace(fen[ch], "♗")
                if fen[ch] == "n":
                    fen = fen.replace(fen[ch], "♘")
                if fen[ch] == "q":
                    fen = fen.replace(fen[ch], "♕")
                if fen[ch] == "k": 
                    fen = fen.replace(fen[ch], "♔")
            if fen[ch].upper():
                if fen[ch] == "R":
                    fen = fen.replace(fen[ch], "♜")
                if fen[ch] == "P":
                    fen = fen.replace(fen[ch], "♟")
                if fen[ch] == "B":
                    fen = fen.replace(fen[ch], "♝")
                if fen[ch] == "N":
                    fen = fen.replace(fen[ch], "♞")
                if fen[ch] == "Q":
                    fen = fen.replace(fen[ch], "♛")
                if fen[ch] == "K": 
                    fen = fen.replace(fen[ch], "♚") 
        parts = fen.split(' ')
        self.all_pieces = [[' ' for _ in range(8)] for _ in range(8)]
        
        rows = parts[0].split('/')
        
        for i in range(8):
            j = 0
            for ch in rows[i]:
                if ch.isdigit():
                    self.all_pieces[i][j:j+int(ch)] = [' '] * int(ch)
                    j += int(ch)
                else:
                    self.all_pieces[i][j] = ch
                    j += 1     

    def print_pos(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    cprint(self.all_pieces[i][j] + " ", 'white', 'on_grey', end='')
                else:
                    cprint(self.all_pieces[i][j] + " ", 'white', 'on_white', end='')
            print()

test = Chess('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
test = Chess("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
test.print_pos()