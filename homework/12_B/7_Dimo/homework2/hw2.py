from enum import Enum
from termcolor import cprint


class Chess_piece(Enum):
    EMPTY = 0 #field is empty
    _VIRGIN_BIT = 1<<4 #piece has moved important for king or queen side castling
    _WHITE = 1<<5 #White field
    _BLACK = 1<<6 # Black field
    _PAWN = 1<<0|_VIRGIN_BIT #interface for the pawn
    _ROOCK = 1<<1|_VIRGIN_BIT #interface for the toock
    _BISHOP = 1<<2|_VIRGIN_BIT #interface for the bishop
    _KNIGHT = 1<<3|_VIRGIN_BIT #interface for the knight
    _KING = _PAWN|_ROOCK|_BISHOP|_VIRGIN_BIT #inteface for the king The pawn tels us it can move only by one field, the roock and bishop bit tels us it can move in diagonal and vertical and horizontal
    _QUEEN = _ROOCK|_BISHOP|_VIRGIN_BIT #interface for the queen 

    #PAWNS
    WPAWN = _PAWN|_WHITE
    BPAWN = _PAWN|_BLACK

    #ROOCKs
    WROOCK = _ROOCK|_WHITE
    BROOCK = _ROOCK|_BLACK

    #BISHOPS
    WBISHOP = _BISHOP|_WHITE
    BBISHOP = _BISHOP|_BLACK

    #KNIGHTS
    WKNIGHT = _KNIGHT|_WHITE
    BKNIGHT = _KNIGHT|_BLACK

    #KINGS
    WKING = _KING|_WHITE
    BKING = _KING|_BLACK

    #QUEENS
    WQUEEN = _QUEEN|_WHITE
    BQUEEN = _QUEEN|_BLACK
    

    

class Chess_position:
    piece:Chess_piece = Chess_piece.EMPTY,
    x:int = 0
    y:int = 0
    _MAP = {
        Chess_piece.EMPTY:" ",
        Chess_piece.WPAWN:"♟",
        Chess_piece.WROOCK:"♜",
        Chess_piece.WBISHOP:"♝",
        Chess_piece.WKNIGHT:"♞",
        Chess_piece.WQUEEN:"♛",
        Chess_piece.WKING:"♚",
        Chess_piece.BPAWN:"♙",
        Chess_piece.BROOCK:"♖",
        Chess_piece.BBISHOP:"♗",
        Chess_piece.BKNIGHT:"♘",
        Chess_piece.BQUEEN:"♕",
        Chess_piece.BKING:"♔"
    }
    def getStringFigure(self):
        
        return self._MAP[self.piece]
    def __init__(self,piece,x,y):
        self.piece = piece
        self.x = x
        self.y = y
class Chess_board:
    field = [
        [Chess_position(Chess_piece.BROOCK,0,0),Chess_position(Chess_piece.BKNIGHT,1,0),Chess_position(Chess_piece.BBISHOP,2,0), Chess_position(Chess_piece.BKING,3,0),Chess_position(Chess_piece.BQUEEN,4,0),Chess_position(Chess_piece.BBISHOP,5,0),Chess_position(Chess_piece.BKNIGHT,6,0),Chess_position(Chess_piece.BROOCK,7,0)],
        [Chess_position(Chess_piece.BPAWN,i,1) for i in range(8)],#faster typing
        [Chess_position(Chess_piece.EMPTY,i,2) for i in range(8)],
        [Chess_position(Chess_piece.EMPTY,i,3) for i in range(8)],
        [Chess_position(Chess_piece.EMPTY,i,4) for i in range(8)],
        [Chess_position(Chess_piece.EMPTY,i,5) for i in range(8)],
        [Chess_position(Chess_piece.WPAWN,i,6) for i in range(8)],
        [Chess_position(Chess_piece.WROOCK,0,7),Chess_position(Chess_piece.WKNIGHT,1,7),Chess_position(Chess_piece.WBISHOP,2,7),Chess_position(Chess_piece.WKING,3,7),Chess_position(Chess_piece.WQUEEN,4,7),Chess_position(Chess_piece.WBISHOP,5,7),Chess_position(Chess_piece.WKNIGHT,6,7),Chess_position(Chess_piece.WROOCK,7,7)]
    ]

    def _getOrder(indexX,indexY):
        return indexX%2 if indexY%2 else ~indexX%2
    def _getOnColor(order):
        return "on_grey" if order else "on_white"
    def _getTextColor(order):
        "white" if order else "grey"
    def PrintIt(self):
        for indexY,line in enumerate(self.field):
            for indexX,figure in enumerate(line):
                order = Chess_board._getOrder(indexX,indexY) #quick check if field is suposed to be white or black/grey used in the ifs to determine color 
                cprint(figure.getStringFigure()+" ", end='',color=Chess_board._getTextColor(order),on_color=Chess_board._getOnColor(order))
            print("")

board = Chess_board()
board.PrintIt()