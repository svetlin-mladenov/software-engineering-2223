class Figure:
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"


class Knight(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"


class Bishop(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"


class Queen(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "K"


class Pawn(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
