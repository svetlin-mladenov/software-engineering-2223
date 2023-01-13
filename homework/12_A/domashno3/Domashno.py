import tkinter as tk
import string 
import os, sys 
from PIL import Image, ImageTk 
from PIL.ImageTk import PhotoImage

class Board(tk.Frame):

    def set_board_from_FEN(self, fen):
    sections = fen.split(" ")
    position = sections[0]
    ranks = position.split("/")
    for i in range(8):
        for j in range(len(ranks[i])):
            if ranks[i][j].isdigit():
                num_empty = int(ranks[i][j])
                j += 1
                for k in range(num_empty):
                    pos = self.ranks[j] + str(8-i)
                    self.squares[pos].config(image="")
                    j += 1
            else:
                pos = self.ranks[j] + str(8-i)
                if ranks[i][j].isupper():
                    self.squares[pos].config(image=self.white_images[ranks[i][j].lower() + ".png"])
                else:
                    self.squares[pos].config(image=self.black_images[ranks[i][j] + ".png"])
                j += 1
    if sections[1] == "w":
        self.turn = "white"
    else:
        self.turn = "black"
fen_str = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
board.set_board_from_FEN(fen_str)

    def __init__(self, parent, length, width): #self=Frame, parent=root
        
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.length = length
        self.width = width
        self.config(height=100*self.length, width=100*self.width)
        self.pack()
        
        self.square_color = None
        self.squares = {} 
        self.ranks = string.ascii_lowercase
        self.white_images = {} 
        self.black_images = {}
        self.white_pieces = ["pyimage1", "pyimage3", "pyimage4", "pyimage5", "pyimage6", "pyimage7"] 
        self.black_pieces = ["pyimage8", "pyimage10", "pyimage11", "pyimage12", "pyimage13", "pyimage14"]
        self.piece_color = None
        self.set_squares()
   
    def set_squares(self): 

        for x in range(8):
            for y in range(8):
                if x%2==0 and y%2==0: 
                    self.square_color="tan4" 
                elif x%2==1 and y%2==1:
                    self.square_color="tan4"
                else:
                    self.square_color="burlywood1"
                    
                B = tk.Button(self, bg=self.square_color, activebackground="lawn green")
                B.grid(row=8-x, column=y)
                pos = self.ranks[y]+str(x+1)
                self.squares.setdefault(pos, B) 
                self.squares[pos].config(command= lambda key=self.squares[pos]: self.select_piece(key))               
        
    def import_pieces(self): 
        path = os.path.join(os.path.dirname(__file__), "White") 
        w_dirs = os.listdir(path)
        for file in w_dirs:
            img = Image.open(path+"\\"+file)
            img = img.resize((80,80), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image=img)
            self.white_images.setdefault(file, img)

        path = os.path.join(os.path.dirname(__file__), "Black") 
        b_dirs = os.listdir(path)
        for file in b_dirs:
            img = Image.open(path+"\\"+file)
            img = img.resize((80,80), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image=img)
            self.black_images.setdefault(file, img)

    def set_pieces(self): 
        dict_rank1_pieces = {"a1":"r.png", "b1":"n.png", "c1":"b.png", "d1":"q.png", "e1":"k.png", "f1":"b.png", "g1":"n.png", "h1":"r.png"} 
        dict_rank2_pieces = {"a2":"p.png", "b2":"p.png", "c2":"p.png", "d2":"p.png", "e2":"p.png", "f2":"p.png", "g2":"p.png", "h2":"p.png"}     
        dict_rank7_pieces = {"a7":"p.png", "b7":"p.png", "c7":"p.png", "d7":"p.png", "e7":"p.png", "f7":"p.png", "g7":"p.png", "h7":"p.png"}
        dict_rank8_pieces = {"a8":"r.png", "b8":"n.png", "c8":"b.png", "d8":"q.png", "e8":"k.png", "f8":"b.png", "g8":"n.png", "h8":"r.png"}

        for key in dict_rank1_pieces: 
            starting_piece = dict_rank1_pieces[key]
            self.squares[key].config(image=self.white_images[starting_piece])
            self.squares[key].image = self.white_images[starting_piece]
            
        for key in dict_rank2_pieces:
            starting_piece = dict_rank2_pieces[key]
            self.squares[key].config(image=self.white_images[starting_piece])
            self.squares[key].image = self.white_images[starting_piece]
            
        for key in dict_rank7_pieces:
            starting_piece = dict_rank7_pieces[key]
            self.squares[key].config(image=self.black_images[starting_piece])
            self.squares[key].image = self.black_images[starting_piece]
            
        for key in dict_rank8_pieces:
            starting_piece = dict_rank8_pieces[key]
            self.squares[key].config(image=self.black_images[starting_piece])
            self.squares[key].image = self.black_images[starting_piece]

        for rank in range(3,7): 
            for file in range(8):
                starting_piece = "blank.png"
                pos = self.ranks[file]+str(rank)
                self.squares[pos].config(image=self.white_images[starting_piece])
                self.squares[pos].image = self.white_images[starting_piece]

root = tk.Tk() 
root.geometry("800x800")
board = Board(root, 8, 8)
board.import_pieces()
board.set_pieces()
board.mainloop()