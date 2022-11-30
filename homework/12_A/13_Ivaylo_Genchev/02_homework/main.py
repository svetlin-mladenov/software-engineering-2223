from table import Colours, Table
from enum import Enum

class Piece(Enum):
    PAWN = '♟'
    BISHOP = '♝' 
    KNIGHT = '♞'
    ROOK = '♜'
    KING = '♚'
    QUEEN = '♛'


def get_tile_colour(x: int, y: int) -> str:
    if (x + y) % 2:
        return colours.GRAY_BG  # black
    else:
        return colours.BROWN_BG # white

def char_table_from_string(str: str) -> Table:
    rows = cols = 0
    
    for line in str.split('\n'):
        rows += 1

        if len(line) > cols:
            cols = len(line)

    table = Table(rows, cols)

    for y, line in enumerate(str.split('\n')):
        for x, char in enumerate(line):
            table.add_cell_value(y, x, char)


    return table

def main():
    chessBoard: Table = char_table_from_string("""\
♜♞♝♛♚♝♞♜
♟♟♟♟♟♟♟♟




♟♟♟♟♟♟♟♟
♜♞♝♛♚♝♞♜""")

    for row in range(chessBoard.rows):
        for col in range(chessBoard.columns):
            colour = get_tile_colour(row, col)

            if row <= 2:
                colour += colours.BLACK_FG
            elif row >= 6:
                colour += colours.WHITE_FG + colours.BOLD

            chessBoard.matrix[row][col].colour_value(colour)

    chessBoard.print()

if __name__ == "__main__":
    colours = Colours()
    main()


