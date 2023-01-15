fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
figures = {'P':'♙','p':'♟','N':'♘','n':'♞','B':'♗','b':'♝','R':'♖','r':'♜','Q':'♕','q':'♛','K':'♔','k':'♚','.':' '}

def parse_fen(fen):
    board = [['.' for _ in range(8)] for _ in range(8)]
    fen_parts = fen.split(" ")
    rows = fen_parts[0].split("/")
    for i in range(8):
        j = 0
        for c in rows[i]:
            if c.isalpha():
                board[i][j] = c
                j += 1
            else:
                for _ in range(int(c)):
                    board[i][j] = '.'
                    j += 1
    return board

board = parse_fen(fen)
for i in range(8,0,-1):
    print(i, " ".join([figures[ch] for ch in board[8-i]]))
print("  a b c d e f g h")
