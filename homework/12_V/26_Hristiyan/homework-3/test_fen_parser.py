import pytest
from fen_parser import parse_fen


def test_valid_fen():
    fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
    board, active_color, castling_rights, en_passant_square, halfmove_clock, fullmove_number = parse_fen(
        fen)
    assert board == [['r', '-', '-', '-', '-', '-', 'r', 'k'],
                     ['-', 'p', '-', 'q', '-', 'p', '-', 'p'],
                     ['p', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', 'N', '-', '-', '-', '-'],
                     ['-', '-', '-', 'P', 'n', 'B', '-', 'b'],
                     ['-', '-', 'P', '-', '-', 'Q', '-', 'P'],
                     ['P', 'P', '-', '-', '-', 'P', '-', '-'],
                     ['R', '-', '-', '-', 'R', '-', '-', 'K']]
    assert active_color == "b"
    assert castling_rights == "-"
    assert en_passant_square == "-"
    assert halfmove_clock == 0
    assert fullmove_number == 25


def test_invalid_fen():
    fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K"
    with pytest.raises(ValueError):
        parse_fen(fen)
