from enum import Enum
from termcolor import cprint


class ChessPiece(Enum):
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
    

    

class ChessPosition:
    piece:ChessPiece = ChessPiece.EMPTY,
    _map = {
        ChessPiece.EMPTY:" ",
        ChessPiece.WPAWN:"♟",
        ChessPiece.WROOCK:"♜",
        ChessPiece.WBISHOP:"♝",
        ChessPiece.WKNIGHT:"♞",
        ChessPiece.WQUEEN:"♛",
        ChessPiece.WKING:"♚",
        ChessPiece.BPAWN:"♙",
        ChessPiece.BROOCK:"♖",
        ChessPiece.BBISHOP:"♗",
        ChessPiece.BKNIGHT:"♘",
        ChessPiece.BQUEEN:"♕",
        ChessPiece.BKING:"♔"
    }
    _map_reverse_translate = {
        "-":ChessPiece.EMPTY,
        "P":ChessPiece.WPAWN,
        "R":ChessPiece.WROOCK,
        "B":ChessPiece.WBISHOP,
        "N":ChessPiece.WKNIGHT,
        "Q":ChessPiece.WQUEEN,
        "K":ChessPiece.WKING,
        "p":ChessPiece.BPAWN,
        "r":ChessPiece.BROOCK,
        "b":ChessPiece.BBISHOP,
        "n":ChessPiece.BKNIGHT,
        "q":ChessPiece.BQUEEN,
        "k":ChessPiece.BKING
    }

    def __str__(self):
        return self._map[self.piece]

    @staticmethod
    def translate(figure:str):
        return ChessPosition(ChessPosition._map_reverse_translate[figure])

    def __init__(self,piece):
        self.piece = piece

    def take_virginity(self):
        self.piece^=ChessPiece._VIRGIN_BIT

    def get_piece(self):
        return self.piece

class Chess_board:
    field = []
    _enpasant_target = ""
    _halfmove_clock = ""
    _fullmove_clock = ""
    _active_player = ""

    @staticmethod
    def _get_order(indexX,indexY):
        return indexX%2 if indexY%2 else ~indexX%2

    @staticmethod
    def _get_on_color(order):
        return "on_grey" if order else "on_white"

    @staticmethod
    def _get_text_color(order):
        "white" if order else "grey"

    def print_metadata(self):
        msg = " and a half" if self._halfmove_clock == 1 else ""
        print(f"Current active player is: {self._active_player}, there is {self._enpasant_target} enpasant target and moves: {self._fullmove_clock + msg}")

    def print(self):
        for indexY,line in enumerate(self.field):
            for indexX,figure in enumerate(line):
                order = Chess_board._get_order(indexX,indexY) #quick check if field is suposed to be white or black/grey used in the ifs to determine color 
                cprint(str(figure)+" ", end='',color=Chess_board._get_text_color(order),on_color=Chess_board._get_on_color(order))
            print("")

    @staticmethod
    def _fen_castling_rights(rights):
        types = ["Q","K","q","k"]
        return_value = [False,False,False,False]
        if rights == "-":
            return return_value
        
        for i in range(len(types)):
            if types[i] in rights:
                return_value[i] = True
        return return_value

    def from_fen(self,representation):
        self.field = []
        representation_items = representation.split(" ")
        field = representation_items[0].split("/")
        self._active_player = representation_items[1]
        castling_righs = self._fen_castling_rights(representation_items[2])
        self._enpasant_target = "no" if representation_items[3] else representation_items[3]
        self._halfmove_clock = representation_items[4]
        self._fullmove_clock = representation_items[5]
        for i in range(len(field)):
            row = []
            for char in field[i]:
                if str.isdigit(char):
                    row+=[ChessPosition(ChessPiece.EMPTY)  for _ in range(int(char))]
                else:
                    translation = ChessPosition.translate(char)
                    if translation.get_piece() == ChessPiece.WKING and castling_righs[0] == True or castling_righs[1] == True:
                        translation.take_virginity()
                    elif translation.get_piece() == ChessPiece.BKING and castling_righs[2] == True or castling_righs[3] == True:
                        translation.take_virginity()
                    row.append(translation)

            self.field.append(row)

        

board = Chess_board()
board.from_fen("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
board.print()
board.print_metadata()