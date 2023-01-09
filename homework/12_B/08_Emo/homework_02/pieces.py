class ChessPiece(object):
    """Superclass for all chess pieces."""

    my_pos = ()
    was_enemy = False #previous position sent to in_bounds was an enemy
    
    def __init__(self, position, color):

        self.my_pos = position
        self.color = color

    def get_my_pos(self):
        return self.my_pos

    def get_color(self):
        return self.color
   
    def __str__(self):
        return self.color

class Pawn(ChessPiece):
   
    def __str__(self):
        return 'Pawn' + super(Pawn, self).__str__()

class Rook(ChessPiece):
    """Class for Rook."""

    def __str__(self):
        return 'Rook' + super(Rook, self).get_color()

class Knight(ChessPiece):

    def __str__(self):
        return 'Knight' + super(Knight, self).__str__()

class Bishop(ChessPiece):

    def __str__(self):
        return 'Bishop' + super(Bishop, self).__str__()

class Queen(ChessPiece):

    def __str__(self):
        return 'Queen' + super(Queen, self).__str__()

class King(ChessPiece):

    def __str__(self):
        return 'King' + super(King, self).__str__()


