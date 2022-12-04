Colors = ["red", "blue"]

class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = Colors[color]

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"


class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"