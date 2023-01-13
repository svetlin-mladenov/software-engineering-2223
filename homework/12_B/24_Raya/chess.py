from termcolor import colored, cprint
 
import colorama # solve problems with termcolor for windows cmd
colorama.init(autoreset = "True")

class Piece: # class for chess piece
    def __init__(self, posX, posY, name, color):
        self.posX = posX
        self.posY = posY
        self.name = name
        self.color = color

class Desk: # class for chess desk
    def __init__(self):
        self.desk = {} #create desk
        for i in range(8): #rows
            key = chr(ord('a') + i) 
            self.desk[key] = []
            for j in range(8): #columns
                if(i == 0 or i == 7):
                    color = ("white" if i == 0 else "grey")
                    if(j == 0 or j == 7):
                        self.desk[key].append(Piece(key, j, "B", color)) #bishop
                    if(j == 1 or j == 6):
                        self.desk[key].append(Piece(key, j, "N", color)) #knight
                    if(j == 2 or j == 5):
                        self.desk[key].append(Piece(key, j, "R", color)) #rook
                    if(j == 3):
                        self.desk[key].append(Piece(key, j, "K", color)) #king
                    if(j == 4):
                        self.desk[key].append(Piece(key, j, "Q", color)) #queen
                elif(i == 1 or i == 6):
                    color = ("white" if i == 1 else "grey")
                    self.desk[key].append(Piece(key, j, "P", color)) #pawn
                else:
                    self.desk[key].append(None) #empty

    def print(self):
        cprint("Legend: ", "green")
        print("B - bishop")
        print("N - knight")
        print("R - rook")
        print("Q - queen")
        print("K - king")
        print("P - pawn")
        print()

        print("  1 2 3 4 5 6 7 8") # column numbers
        for key in self.desk.keys():
            print(key + " ", end = '') # row numbers
            for i in range(8):
                try:
                    cprint(self.desk[key][i].name, self.desk[key][i].color, "on_red", end = '')
                    cprint(" ", "grey", "on_red", end = '')
                except:
                    cprint("X ", "grey", "on_red", end = '')
            print()

  

desk = Desk()


desk.print()