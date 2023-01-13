from termcolor import colored

class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = color

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("R", color)


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("N", color)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("B", color)


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("Q", color)


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("K", color)


class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("GP", color)


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = colored("P", color)

def setup_chess_pieces(color):
    """
    Helper function to set up chess pieces on the board
    """
    pieces = []
    # add pawns
    for i in range(8):
        pieces.append(Pawn(color))
    # add other pieces
    pieces.append(Rook(color))
    pieces.append(Knight(color))
    pieces.append(Bishop(color))
    pieces.append(Queen(color))
    pieces.append(King(color))
    pieces.append(Bishop(color))
    pieces.append(Knight(color))
    pieces.append(Rook(color))
    return pieces