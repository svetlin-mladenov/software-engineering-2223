from ChessPieces import ChessPiece, King, Queen, Rook, Bishop, Knight, Pawn
from EnumChessPiece import EnumChessPiece
from termcolor import colored

class ChessBoard:
  # Initialize starting board matrix
  def __init__(self): 
    self.board = []
    for i in range(8):
      self.board.append([])
      for _ in range(8):
        self.board[i].append(None)

    # Setting starting chessboard pieces' positions
    self.board[0][0] = Rook(EnumChessPiece.BLACK_ROOK)
    self.board[0][1] = Knight(EnumChessPiece.BLACK_KNIGHT)
    self.board[0][2] = Bishop(EnumChessPiece.BLACK_BISHOP)
    self.board[0][3] = Queen(EnumChessPiece.BLACK_QUEEN)
    self.board[0][4] = King(EnumChessPiece.BLACK_KING)
    self.board[0][5] = Bishop(EnumChessPiece.BLACK_BISHOP)
    self.board[0][6] = Knight(EnumChessPiece.BLACK_KNIGHT)
    self.board[0][7] = Rook(EnumChessPiece.BLACK_ROOK)

    for i in range(8):
      self.board[1][i] = Pawn(EnumChessPiece.BLACK_PAWN)
      self.board[6][i] = Pawn(EnumChessPiece.WHITE_PAWN)

    self.board[7][0] = Rook(EnumChessPiece.WHITE_ROOK)
    self.board[7][1] = Knight(EnumChessPiece.WHITE_KNIGHT)
    self.board[7][2] = Bishop(EnumChessPiece.WHITE_BISHOP)
    self.board[7][3] = Queen(EnumChessPiece.WHITE_QUEEN)
    self.board[7][4] = King(EnumChessPiece.WHITE_KING)
    self.board[7][5] = Bishop(EnumChessPiece.WHITE_BISHOP)
    self.board[7][6] = Knight(EnumChessPiece.WHITE_KNIGHT)
    self.board[7][7] = Rook(EnumChessPiece.WHITE_ROOK)

    self.display_board = self.__build_display_board() # Building the border around the chessboard for the UI
    self.__conversion_board = self.__build_conversion_board() # Dictionary that translates where each piece should go on the UI board

    self.__update_display_board()

  # Translate matrix coordinates to chessboard positions and returns a dictionary
  #def __map_matrix_coordinates_to_position(self):
  #  keys = []
  #  values = []
  #
  #  for i in range(len(self.board)):
  #    for j in range(len(self.board[i])):
  #      keys.append((i, j))
  #      values.append((chr(ord('a') + j) + str(8 - i)))
  #
  #  return dict(zip(keys, values))

  # Building the blank chessboard border for the UI filling it up with pieces
  def __build_display_board(self):
    display_board = ""
    # Printing first row of squares
    display_board += "  ┌" # Top Left of board
    for i in range(9):
      if i == 8:
        display_board += "  └" # Bottom left of board
      for j in range(8):
        for _ in range(4):
          display_board += "─" # Top middle/bottom middle separator between boxes

        # Printing last symbol of each row of squares
        if j == 7:
          if i == 0: # last symbol on top row of squares a.k.a. top right of board
            display_board += "┐\n"
          elif(i == 8): # last symbol on bottom row of squares a.k.a. bottom left of board
            display_board += "┘\n"
            break
          else: # last symbol on middle rows of squares a.k.a. top right/bottom right border of last column boxes
            display_board += "┤\n"
          break
        
        # Building separators in between boxes that appear top right, top, left, bottom left and bottom right of each box
        if i == 0:
          display_board += "┬" # first row of boxes
        elif i == 8:
          display_board += "┴" # last row of boxes
        else:
          display_board += "┼" # middle rows of boxes

      if i == 8: # board is finished
        break

      display_board += str(8 - i) + " │" # Numbers left of the board to assist beginners in finding position

      # Prints middle of each square and it's walls/side borders
      for _ in range(8):
        for _ in range(4):
          display_board += " " # Blank space in each box, which might contain a piece
        display_board += "│" # Print walls/side borders of each square
        
      display_board += "\n"
      if i != 7:
        display_board += "  ├" # Print bottom left/top left border for the first column of boxes

    # Letters under the board to assist beginners in finding position names
    for i in range(8):
      display_board += "    "
      display_board += chr(ord('A') + i)
    display_board += '\n'
    return display_board

  # Helps with filling UI board with pieces
  def __build_conversion_board(self):
    keys = []
    values = []

    index = 48 # Display board index
    for i in range(8):
      for j in range(8):
        keys.append(index)
        values.append((i, j))
        index += 5
      index += 48
  
    return dict(zip(keys, values))

  # Converts board to given FEN position
  def FENparser(self, pos):
    # Converts string to array by splitting each rank from the chess board a.k.a.
    # separates string using separator '/', which separates each chess board rank 1-8
    rows = pos.split("/")

    # Clean chessboard
    self.board = [[None for _ in i] for i in self.board]

    for i in range(len(rows)):
      k = 0
      for j in range(len(rows[i])):
        if rows[i][j] == ' ': # End of chess position
          break
        elif rows[i][j] in '12345678': # Blank square
          k += int(rows[i][j])
          # !!!!!!!!!!!!!!!!!!!!!!!!!!

        else: # A piece
          self.board[i][k] = ChessPiece(notation = rows[i][j])
          k += 1
    self.__update_display_board()

  # Update UI board by updating piece positions
  def __update_display_board(self):
    s = self.display_board
    for key in self.__conversion_board:
      row_index = self.__conversion_board[key][0]
      column_index = self.__conversion_board[key][1]

      if(self.board[row_index][column_index] != None):
        start = s[:key]
        end = s[key + 1:]
        s = start + self.board[row_index][column_index].display_icon + end
      else:
        start = s[:key]
        end = s[key + 1:]
        s = start + ' ' + end        

    self.display_board = s

  # Print UI board
  def print_display_board(self):
    print("\n" + colored(self.display_board, 'cyan') + "\n")