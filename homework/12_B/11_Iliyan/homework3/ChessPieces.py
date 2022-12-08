from ChessPiece import ChessPiece

class King(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)

class Queen(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)

class Rook(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)

class Bishop(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)

class Knight(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)
    
  def _determine_notation(self):
    if(self.colour == "White"):
      return self.name[1].upper()
    
    return self.name[1]

class Pawn(ChessPiece):
  def __init__(self, colour_name=None, notation=None):
    super().__init__(colour_name, notation)