from enum import Enum
from dataclasses import dataclass
from termcolor import colored
    
    
class PieceColour(Enum):
    WHITE  = "blue"
    BLACK  = "red"

class TileColour(Enum):
    WHITE  = "on_white"
    BLACK  = "on_grey"


class PieceType(Enum):
    PAWN   = "♟"
    ROOK   = "♜"
    KNIGHT = "♞"
    BISHOP = "♝"
    KING   = "♚"
    QUEEN  = "♛"

    
@dataclass
class Piece:
    pieceType: PieceType = PieceType.PAWN
    pieceColour: PieceColour = PieceColour.WHITE
    

@dataclass
class ChessTile:
    tileColour: TileColour
    chessPiece:Piece = None
    
    def __init__(self, x: int, y: int):
        self.tileColour = TileColour.BLACK if ((x + y) % 2) == 1 else TileColour.WHITE
        
    
    def print(self) -> None:
        text = ' ' if self.chessPiece is None else self.chessPiece.pieceType.value
        colour = None if self.chessPiece is None else self.chessPiece.pieceColour.value
        
        print(colored(" " + text + " ", attrs=["bold"] , color=colour, on_color=self.tileColour.value), end='')
        

class ChessBoard:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.field = []
        for i in range(width):
            col = []
            for j in range(height):
                col.append(ChessTile(x=i, y=j))
            self.field.append(col)
            
    def set_game(self) -> None:
        for i in range(self.width):
            self.field[1][i].chessPiece = Piece(pieceColour=PieceColour.BLACK)
            self.field[self.height-2][i].chessPiece = Piece(pieceColour=PieceColour.WHITE)
        
        
        # ROOKS
        self.field[0][0].chessPiece = Piece(pieceType= PieceType.ROOK, pieceColour=PieceColour.BLACK)
        self.field[0][self.height-1].chessPiece = Piece(pieceType= PieceType.ROOK, pieceColour=PieceColour.BLACK)
        self.field[self.width-1][0].chessPiece = Piece(pieceType= PieceType.ROOK, pieceColour=PieceColour.WHITE)
        self.field[self.width-1][self.height-1].chessPiece = Piece(pieceType= PieceType.ROOK, pieceColour=PieceColour.WHITE)
        
        # KNIGHTS
        self.field[0][1].chessPiece = Piece(pieceType= PieceType.KNIGHT, pieceColour=PieceColour.BLACK)
        self.field[0][self.height-2].chessPiece = Piece(pieceType= PieceType.KNIGHT, pieceColour=PieceColour.BLACK)
        self.field[self.width-1][1].chessPiece = Piece(pieceType= PieceType.KNIGHT, pieceColour=PieceColour.WHITE)
        self.field[self.width-1][self.height-2].chessPiece = Piece(pieceType= PieceType.KNIGHT, pieceColour=PieceColour.WHITE)
        
        # BISHOPS
        self.field[0][2].chessPiece = Piece(pieceType= PieceType.BISHOP, pieceColour=PieceColour.BLACK)
        self.field[0][self.height-3].chessPiece = Piece(pieceType= PieceType.BISHOP, pieceColour=PieceColour.BLACK)
        self.field[self.width-1][2].chessPiece = Piece(pieceType= PieceType.BISHOP, pieceColour=PieceColour.WHITE)
        self.field[self.width-1][self.height-3].chessPiece = Piece(pieceType= PieceType.BISHOP, pieceColour=PieceColour.WHITE)
        
        # QUEENS
        self.field[0][3].chessPiece = Piece(pieceType= PieceType.QUEEN, pieceColour=PieceColour.BLACK)
        self.field[self.width-1][3].chessPiece = Piece(pieceType= PieceType.QUEEN, pieceColour=PieceColour.WHITE)
        
        # KINGS
        self.field[0][self.height-4].chessPiece = Piece(pieceType= PieceType.KING, pieceColour=PieceColour.BLACK)
        self.field[self.width-1][self.height-4].chessPiece = Piece(pieceType= PieceType.KING, pieceColour=PieceColour.WHITE)
        

def main() -> None:
    chessBoard = ChessBoard(8, 8)
    chessBoard.set_game()
    
    for i in chessBoard.field:
        for j in i:
            j.print()
        print()
        
if __name__ == "__main__":
    main()
