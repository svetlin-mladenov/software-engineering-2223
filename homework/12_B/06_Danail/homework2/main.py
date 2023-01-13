class Figure:
    name = None
    icon = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


class WhitePawn(Figure):
    name = 'White Pawn'
    icon = '♙'


class BlackPawn(Figure):
    name = 'Black Pawn'
    icon = '♟️'


class WhiteRook(Figure):
    name = 'White Rook'
    icon = '♖'


class BlackRook(Figure):
    name = 'Black Rook'
    icon = '♜'


class WhiteKnight(Figure):
    name = 'White Knight'
    icon = '♘'


class BlackKnight(Figure):
    name = 'Black Knight'
    icon = '♞'


class WhiteBishop(Figure):
    name = 'White Bishop'
    icon = '♗'


class BlackBishop(Figure):
    name = 'Black Bishop'
    icon = '♝'


class WhiteQueen(Figure):
    name = 'White Queen'
    icon = '♕'


class BlackQueen(Figure):
    name = 'Black Queen'
    icon = '♛'


class WhiteKing(Figure):
    name = 'White King'
    icon = '♔'


class BlackKing(Figure):
    name = 'Black King'
    icon = '♚'


chessboard = list()


w_rook_1 = WhiteRook(1, 1)
w_knight_1 = WhiteKnight(2, 1)
w_bishop_1 = WhiteBishop(3, 1)
w_queen = WhiteQueen(4, 1)
w_king = WhiteKing(5, 1)
w_bishop_2 = WhiteBishop(6, 1)
w_knight_2 = WhiteKnight(7, 1)
w_rook_2 = WhiteRook(8, 1)
w_pawn_1 = WhitePawn(1, 2)
w_pawn_2 = WhitePawn(2, 2)
w_pawn_3 = WhitePawn(3, 2)
w_pawn_4 = WhitePawn(4, 2)
w_pawn_5 = WhitePawn(5, 2)
w_pawn_6 = WhitePawn(6, 2)
w_pawn_7 = WhitePawn(7, 2)
w_pawn_8 = WhitePawn(8, 2)

b_rook_1 = BlackRook(1, 8)
b_knight_1 = BlackKnight(2, 8)
b_bishop_1 = BlackBishop(3, 8)
b_queen = BlackQueen(4, 8)
b_king = BlackKing(5, 8)
b_bishop_2 = BlackBishop(6, 8)
b_knight_2 = BlackKnight(7, 8)
b_rook_2 = BlackRook(8, 8)
b_pawn_1 = BlackPawn(1, 7)
b_pawn_2 = BlackPawn(2, 7)
b_pawn_3 = BlackPawn(3, 7)
b_pawn_4 = BlackPawn(4, 7)
b_pawn_5 = BlackPawn(5, 7)
b_pawn_6 = BlackPawn(6, 7)
b_pawn_7 = BlackPawn(7, 7)
b_pawn_8 = BlackPawn(8, 7)

chessboard.append(w_rook_1)
chessboard.append(w_knight_1)
chessboard.append(w_bishop_1)
chessboard.append(w_queen)
chessboard.append(w_king)
chessboard.append(w_bishop_2)
chessboard.append(w_knight_2)
chessboard.append(w_rook_2)
chessboard.append(w_pawn_1)
chessboard.append(w_pawn_2)
chessboard.append(w_pawn_3)
chessboard.append(w_pawn_4)
chessboard.append(w_pawn_5)
chessboard.append(w_pawn_6)
chessboard.append(w_pawn_7)
chessboard.append(w_pawn_8)

chessboard.append(b_rook_1)
chessboard.append(b_knight_1)
chessboard.append(b_bishop_1)
chessboard.append(b_queen)
chessboard.append(b_king)
chessboard.append(b_bishop_2)
chessboard.append(b_knight_2)
chessboard.append(b_rook_2)
chessboard.append(b_pawn_1)
chessboard.append(b_pawn_2)
chessboard.append(b_pawn_3)
chessboard.append(b_pawn_4)
chessboard.append(b_pawn_5)
chessboard.append(b_pawn_6)
chessboard.append(b_pawn_7)
chessboard.append(b_pawn_8)

for y in range(1, 9):
    print('', end='|')
    for x in range(1, 9):
        flag = False
        for figure in chessboard:
            if figure.x == x and figure.y == y:
                flag = True
                print(f'{figure.icon}', end='|')
                break
        if not flag:
            print(' ', end='|')
    print(' ')
