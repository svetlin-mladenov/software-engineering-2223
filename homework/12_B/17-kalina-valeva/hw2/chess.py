from dataclasses import dataclass

whiteKing = "♔"
whiteQueen = "♕"
whiteRook = "♖"
whiteBishop = "♗"
whiteHorse = "♘"
whitePawn = "♙"
blackKing = "♚"
blackQueen = "♛"
blackRook = "♜"
blackBishop = "♝"
blackHorse = "♞"
blackPawn = "♟︎"

@dataclass
class Figura:
  value: str = "[]"

  def __str__(self):
    return self.value

class Duska:
    figuri = [Figura(whiteRook), Figura(whiteHorse), Figura(whiteBishop),Figura(whiteQueen), Figura(whiteKing), Figura(whiteBishop), Figura(whiteHorse), Figura(whiteRook)] + [Figura(whitePawn)] * 8 + [Figura()] * 32 + [Figura(blackPawn)] * 8 + [Figura(blackRook), Figura(blackHorse), Figura(blackBishop),Figura(blackKing), Figura(blackQueen), Figura(blackBishop), Figura(blackHorse), Figura(blackRook)]
    def print(self):
        for i in range(64):
            print(self.figuri[i], end = chr(9) if (i+1) % 8 != 0 else '\n')


Duska().print()