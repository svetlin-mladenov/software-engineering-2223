from EnumChessPiece import EnumChessPiece

class ChessPiece:
  def __init__(self, colour_name=None, notation=None):
    if colour_name is not None:
      # Setting class attributes
      self.colour = str(colour_name.name).split("_")[0].capitalize()
      self.name = str(colour_name.name).split("_")[1].capitalize()
      self.value = colour_name.value[1]
      self.display_icon = colour_name.value[0]

      self.notation = self._determine_notation()
    else: # NOTATION GIVEN CASE
      notation_to_colourName = {"K" : "KING", 
                                "Q" : "QUEEN", 
                                "R" : "ROOK", 
                                "B" : "BISHOP", 
                                "N" : "KNIGHT", 
                                "P" : "PAWN"}

      if notation.isupper():
        colour_name = "WHITE_"
      else:
        colour_name = "BLACK_"
      
      colour_name += notation_to_colourName[notation.upper()]

      # Setting class attributes
      self.colour = str(EnumChessPiece[colour_name].name).split("_")[0].capitalize()
      self.name = str(EnumChessPiece[colour_name].name).split("_")[1].capitalize()
      self.value = EnumChessPiece[colour_name].value[1]
      self.display_icon = EnumChessPiece[colour_name].value[0]

      self.notation = notation

  # Determines FEN notation of the piece. Ex: 
  # White King -> K, White Knight -> N, White Pawn -> P
  # Black King -> k, Black Knight -> n, Black Pawn -> p, etc.
  def _determine_notation(self):
    if(self.colour == "White"):
      return self.name[0]
    
    return self.name[0].lower()