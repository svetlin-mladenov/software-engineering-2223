from termcolor import colored, cprint
import math

 
import colorama # solve problems with termcolor for windows cmd
colorama.init(autoreset = "True")

class Piece: # class for chess piece
    def __init__(self, posX = 0, posY = 0, name = "", color = "white"):
        self.posX = posX
        self.posY = posY
        self.name = name
        self.color = color


class Desk: # class for chess desk
    def __init__(self):
        self.desk = {} #create desk
        for i in range(8): #rows
            self.desk[i] = []
            for j in range(8): #columns
                key = chr(ord('a') + j) 

                self.desk[i].append(Piece(key, j)) #empty
        

    def StartingPosition(self):
        for i in range(8): #rows
            for j in range(8): #columns
                key = chr(ord('a') + j) 
                if(i == 0 or i == 7):
                    color = ("white" if i == 0 else "grey")
                    if(j == 0 or j == 7):
                        self.desk[i].append(Piece(j, key, "R", color)) #bishop
                    if(j == 1 or j == 6):
                        self.desk[i].append(Piece(j, key, "N", color)) #knight
                    if(j == 2 or j == 5):
                        self.desk[i].append(Piece(j, key, "B", color)) #rook
                    if(j == 3):
                        self.desk[i].append(Piece(j, key, "Q", color)) #king
                    if(j == 4):
                        self.desk[i].append(Piece(j, key, "K", color)) #queen
                elif(i == 1 or i == 6):
                    color = ("white" if i == 1 else "grey")
                    self.desk[i].append(Piece(key, j, "P", color)) #pawn
          

    def print(self):
        cprint("Legend: ", "green")
        print("B - bishop")
        print("N - knight")
        print("R - rook")
        print("Q - queen")
        print("K - king")
        print("P - pawn")
        print()

        print("  a b c d e f g h ") # column numbers
        for key in self.desk.keys():
            print(str(key) + " ", end = '') # row numbers
            for i in range(8):
                if(self.desk[key][i].name != ""):
                    cprint(self.desk[key][i].name, self.desk[key][i].color, "on_red", end = '')
                    cprint(" ", "grey", "on_red", end = '')
                else:
                    cprint("X ", "grey", "on_red", end = '')
            print()
                

    def readFEN(self, fen):
        row = 0
        column = 0
        for i in range(len(fen)):
            if(fen[i].isnumeric()):
                column += int(fen[i])
                continue
            if(fen[i] == ' '):
                break
            if(fen[i] == '/'):
                row+=1;
                column = 0
                continue
            self.desk[row][column].name = fen[i].upper()
            self.desk[row][column].color = ("white" if fen[i].isupper() else "grey")
            column+=1
                

  

desk = Desk()

desk.readFEN("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
desk.print()