

class ChessPiece():

    def __init__(this, symbol):
        this.symbol = symbol


class King(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return King("♚")

    @staticmethod
    def get_black():
        return King("♔") 

class Queen(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return Queen("♛")

    @staticmethod
    def get_black():
        return Queen("♕") 

class Rook(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return Rook("♜")

    @staticmethod
    def get_black():
        return Rook("♖") 

class Bishop(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return Bishop("♝")

    @staticmethod
    def get_black():
        return Bishop("♗") 

class Knight(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return Knight("♞")

    @staticmethod
    def get_black():
        return Knight("♘") 

class Pawn(ChessPiece):

    def __init__(self, symbol):
        ChessPiece.__init__(self, symbol)

    @staticmethod
    def get_white():
        return Pawn("♟")

    @staticmethod
    def get_black():
        return Pawn("♙") 