class ChessPiece:
  def __init__(self, colour_name, position):
    # Check if given position is valid
    position = position.lower()
    
    if len(position) != 2 :
      raise Exception("Invalid piece position given! Must be represented by 2 symbols [letter, number]!")
    
    elif(not((ord(position[0]) >= ord('a') and ord(position[0]) <= ord('h')) and 
             (int(position[1]) >= 1 and int(position[1]) <= 8))):
      raise Exception("Invalid piece position given!")

    # Setting class attributes
    self.colour = str(colour_name.name).split("_")[0].capitalize()
    self.name = str(colour_name.name).split("_")[1].capitalize()
    self.position = position
    self.value = colour_name.value[1]
    self.display_icon = colour_name.value[0]

    self.notation = self._determine_notation()
  
  # Determines notation of piece. Ex: King on e4 -> Ke4, Knight on a7 -> Na7, Pawn on c5 -> c5 etc.
  def _determine_notation(self):
    return self.name[0].upper() + self.position