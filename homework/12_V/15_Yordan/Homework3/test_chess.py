from chess import Chess
import pytest

def test():
    chess = Chess()
    assert chess.board[0][0].name == 'rook'
    assert chess.board[0][0].color == 'white'
    assert chess.getPositionCoordinates('a1') == [0, 0]
    assert chess.getPositionCoordinates('h8') == [7, 7]