def parse_fen(fen):
    parts = fen.strip().split(" ")
    if len(parts) != 6:
        raise ValueError(
            "Invalid FEN string. Must contain 6 space-separated fields.")
    board = [['-' for _ in range(8)] for _ in range(8)]
    rows = parts[0].split("/")
    if len(rows) != 8:
        raise ValueError("Invalid board in FEN string. Must contain 8 rows.")
    for i in range(8):
        j = 0
        for c in rows[i]:
            if c.isnumeric():
                j += int(c)
            else:
                if c.upper() not in "PNBRQK":
                    raise ValueError("Invalid chess piece " +
                                     c+" in FEN string.")
                board[i][j] = c
                j += 1
    active_color = parts[1]
    if active_color not in ["w", "b"]:
        raise ValueError(
            "Invalid active color in FEN string. Must be 'w' or 'b'.")
    castling_rights = parts[2]
    if not all(c in ["K", "Q", "k", "q", "-"] for c in castling_rights):
        raise ValueError(
            "Invalid castling rights in FEN string. Must be in the format of KQkq or '-'.")
    en_passant_square = parts[3]
    if en_passant_square != "-":
        if not all(c in ["a", "b", "c", "d", "e", "f", "g", "h"] for c in en_passant_square[:-1]) or en_passant_square[-1] not in ["3", "6"]:
            raise ValueError(
                "Invalid en passant square in FEN string. Must be in the format of file(a-h) + rank(3 or 6).")
    halfmove_clock = int(parts[4])
    if not isinstance(halfmove_clock, int) or halfmove_clock < 0:
        raise ValueError(
            "Invalid halfmove clock in FEN string. Must be a non-negative integer.")
    fullmove_number = int(parts[5])
    if not isinstance(fullmove_number, int) or fullmove_number <= 0:
        raise ValueError(
            "Invalid fullmove number in FEN string. Must be a positive integer.")
    return (board, active_color, castling_rights, en_passant_square, halfmove_clock, fullmove_number)


def main():
    fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
    board, active_color, castling_rights, en_passant_square, halfmove_clock, fullmove_number = parse_fen(
        fen)
    for row in board:
        for cell in row:
            print(cell, end = " ")
        print()


main()
