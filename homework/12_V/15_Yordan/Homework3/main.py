from chess import Chess

def main():
    chess = Chess()
    chess.printBoard()
    chess.parseFEN('r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25')
    print("\nAfter parsing FEN:\n")
    chess.printBoard()


if __name__ == "__main__":
    main()
