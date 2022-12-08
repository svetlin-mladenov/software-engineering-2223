class Rook():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♜"
        else:
            self.symbol = "♖"


class Knight():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♞"
        else:
            self.symbol = "♘"


class Bishop():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♝"
        else:
            self.symbol = "♗"

class Queen():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♛"
        else:
            self.symbol = "♕"

class King():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♚"
        else:
            self.symbol = "♔"

class Pawn():
    def __init__(self,color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♟"
        else:
            self.symbol = "♙"

