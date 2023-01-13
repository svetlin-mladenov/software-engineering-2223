

chess= {
    "K": "♔",
    "Q": "♕",
    "R": "♖",
    "B": "♗",
    "N": "♘",
    "P": "♙",
    "k": "♚",
    "q": "♛",
    "r": "♜",
    "b": "♝",
    "n": "♞",
    "p": "♟︎"
}
    
class Duska:

    def __init__(self):
        self.figuri = []
        self.count = 0
        
    def read_FEN(self, str):
        for s in str:
            if(s != " "):
                if(s != "/"):
                    if(s.isdigit() == False):
                        self.figuri.append((chess[s]))
                        self.count = self.count + 1
                    else:
                        for i in range(int(s)):
                            self.figuri.append('X')
                        self.count = self.count + int(s)
            else:
                return
            
    def print(self):
        for i in range(64):
            print(self.figuri[i], end = ' ' if (i+1) % 8 != 0 else '\n')

d = Duska()
d.read_FEN("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
d.print()


