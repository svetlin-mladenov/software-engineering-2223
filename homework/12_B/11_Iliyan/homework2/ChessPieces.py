from ChessPiece import ChessPiece

class King(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)

class Queen(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)

class Rook(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)

class Bishop(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)

class Knight(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)
    
  def _determine_notation(self):
    return self.name[1].upper() + self.position

class Pawn(ChessPiece):
  def __init__(self, colour_name, position):
      super().__init__(colour_name, position)

  def _determine_notation(self):
    return self.position