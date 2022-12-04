from termcolor import cprint
import colorama
colorama.init()


class Piece:
    def __init__(self, name, color):
        if color not in ["white", "black"]:
            raise Exception("Invalid color")
        if name == "pawn":
            if color == 'white':
                self.symbol = '♙'
            elif color == 'black':
                self.symbol = '♟'
        elif name == "rook":
            if color == 'white':
                self.symbol = '♖'
            elif color == 'black':
                self.symbol = '♜'
        elif name == "knight":
            if color == 'white':
                self.symbol = '♘'
            elif color == 'black':
                self.symbol = '♞'
        elif name == "bishop":
            if color == 'white':
                self.symbol = '♗'
            elif color == 'black':
                self.symbol = '♝'
        elif name == "queen":
            if color == 'white':
                self.symbol = '♕'
            elif color == 'black':
                self.symbol = '♛'
        elif name == "king":
            if color == 'white':
                self.symbol = '♔'
            elif color == 'black':
                self.symbol = '♚'
        else:
            raise ValueError("Invalid piece name")
        self.name = name
        self.color = color


class Chess:
    def __init__(self):
        # Define empty board 8x8
        self.board = [
            #  a     b     c     d     e     f     g     h
            [None, None, None, None, None, None, None, None],   # 8
            [None, None, None, None, None, None, None, None],   # 7
            [None, None, None, None, None, None, None, None],   # 6
            [None, None, None, None, None, None, None, None],   # 5
            [None, None, None, None, None, None, None, None],   # 4
            [None, None, None, None, None, None, None, None],   # 3
            [None, None, None, None, None, None, None, None],   # 2
            [None, None, None, None, None, None, None, None]    # 1
        ]

        # Initialize the board with pieces - default chess position
        self.addPiece(Piece("rook", "black"), "a8")
        self.addPiece(Piece("knight", "black"), "b8")
        self.addPiece(Piece("bishop", "black"), "c8")
        self.addPiece(Piece("queen", "black"), "d8")
        self.addPiece(Piece("king", "black"), "e8")
        self.addPiece(Piece("bishop", "black"), "f8")
        self.addPiece(Piece("knight", "black"), "g8")
        self.addPiece(Piece("rook", "black"), "h8")
        self.addPiece(Piece("pawn", "black"), "a7")
        self.addPiece(Piece("pawn", "black"), "b7")
        self.addPiece(Piece("pawn", "black"), "c7")
        self.addPiece(Piece("pawn", "black"), "d7")
        self.addPiece(Piece("pawn", "black"), "e7")
        self.addPiece(Piece("pawn", "black"), "f7")
        self.addPiece(Piece("pawn", "black"), "g7")
        self.addPiece(Piece("pawn", "black"), "h7")

        self.addPiece(Piece("pawn", "white"), "a2"),
        self.addPiece(Piece("pawn", "white"), "b2"),
        self.addPiece(Piece("pawn", "white"), "c2"),
        self.addPiece(Piece("pawn", "white"), "d2"),
        self.addPiece(Piece("pawn", "white"), "e2"),
        self.addPiece(Piece("pawn", "white"), "f2"),
        self.addPiece(Piece("pawn", "white"), "g2"),
        self.addPiece(Piece("pawn", "white"), "h2"),
        self.addPiece(Piece("rook", "white"), "a1")
        self.addPiece(Piece("knight", "white"), "b1"),
        self.addPiece(Piece("bishop", "white"), "c1"),
        self.addPiece(Piece("queen", "white"), "d1"),
        self.addPiece(Piece("king", "white"), "e1"),
        self.addPiece(Piece("bishop", "white"), "f1"),
        self.addPiece(Piece("knight", "white"), "g1"),
        self.addPiece(Piece("rook", "white"), "h1"),

    def getPositionCoordinates(self, position):
        if not isinstance(position, str) or \
                len(position) != 2 or \
                position[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] or \
                position[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            raise Exception('Invalid position "{}"! It must be in chess notation like "A1" or "h8"'.format(position))

        return [ord(position[0].lower()) - ord('a'), (ord(position[1]) - ord('1'))]

    def addPiece(self, piece, position):
        if not isinstance(piece, Piece):
            raise Exception('Invalid piece type!')
        coordinates = self.getPositionCoordinates(position)
        self.board[coordinates[0]][coordinates[1]] = piece

    def printBoard(self):
        cprint(' abcdefgh ', 'white', 'on_grey', attrs=['dark'])
        for i in range(7, -1, -1):
            cprint(i + 1, 'white', 'on_grey', attrs=['dark'], end='')
            for j in range(0, 8):
                cell_color = 'on_white'
                if (i + j) % 2 == 0:
                    cell_color = 'on_grey'
                piece = self.board[j][i]
                if piece:
                    cprint(piece.symbol, 'white', cell_color, attrs=['dark'], end='')
                else:
                    cprint(' ', 'white', cell_color, attrs=['dark'], end='')
            cprint(i + 1, 'white', 'on_grey', attrs=['dark'])
        cprint(' abcdefgh ', 'white', 'on_grey', attrs=['dark'])
