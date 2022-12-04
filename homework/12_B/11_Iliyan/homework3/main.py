from ChessBoard import ChessBoard

# Print starting chess position
b = ChessBoard()
b.print_display_board()

# Print given FEN position
FEN_pos = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
b.FENparser(FEN_pos)
b.print_display_board()