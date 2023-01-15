from dataclasses import dataclass,field
from enum import Enum

from termcolor import colored, cprint


def make_a_list(i):
        new_list = [] 
        for f in range(4):
            if i%2 == 0:
                new_list.append( ChessFigure(Color.BLACK, Figure.NONE,f,i))
                new_list.append(ChessFigure(Color.WHITE, Figure.NONE,f+1,i))
            else:
                new_list.append(ChessFigure(Color.WHITE, Figure.NONE,f,i))
                new_list.append( ChessFigure(Color.BLACK, Figure.NONE,f+1,i))
        return new_list

class Figure(Enum):
   KING =" KING "
   QUEEN ="QUEEN "
   ROOK  =" ROOK " 
   BISHOP ="BISHOP"
   KNIGHT ="KNIGHT"	
   PAWN  =" PAWN " 
   NONE ="NONE"

class Color(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"

@dataclass(frozen=True)
# class Chess_Position:
class ChessFigure:
    type: Color
    figure: Figure
    number: int
    letter: str
    
    
@dataclass
class ChessPosition:
    figures: list[ChessFigure] = field(default_factory=list)

    def print_position(self):
        for column in self.figures:
            print()
            print()
            for row in column :  
                if row.type.value is "WHITE":
                    if row.figure.value is "NONE":
                        cprint("      ", "blue" ,"on_white",  end = ' ')

                    else: 
                        cprint(row.figure.value, "blue" ,  end = ' ')
                        
                else:
                    if row.figure.value is "NONE":
                        cprint("      ","red" , "on_magenta", end = ' ')
                    else:
                        cprint(row.figure.value,"red" , end = ' ')
                        
                    # continue
    
    def add_figure(self,new_figure: ChessFigure) -> None:
        y = new_figure.number
        x = ord(new_figure.letter)-(ord("a")-1)
        if self.figures[x-1][y-1].figure.value is "NONE":
            self.figures[x-1][y-1] = new_figure


    def new_position(self):
        self.figures = [make_a_list(i) for i in range(8)]
