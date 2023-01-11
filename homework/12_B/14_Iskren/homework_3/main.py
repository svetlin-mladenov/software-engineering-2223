import termcolor

figures_map = {
    'r': ' ♜  ',
    'n': ' ♞  ',
    'b': ' ♝  ',
    'q': ' ♛  ',
    'k': ' ♚  ',
    'p': ' ♟  ',
    'R': ' ♖  ',
    'N': ' ♘  ',
    'B': ' ♗  ',
    'Q': ' ♕  ',
    'K': ' ♔  ',
    'P': ' ♙  ',
}

class ChessBoard:
    def __init__(self, width, height, fen):
        self.width = width
        self.height = height
        self.fen = fen

        self.board = [[[] for _ in range(self.width)] for _ in range(self.height)]

        self.color_board()
        self.populate_figures()

    def color_board(self):
        for i in range(0, self.height):
            initial_color = (1 if i % 2 else 0) 
            color = initial_color

            for j in range(0, self.width):

                self.board[i][j].append(color)

                color = (initial_color if j % 2 else (1 if initial_color == 0 else 0)) 

    def populate_figures(self):
        def fen_parser(fen):
            fen_list = fen.split(" ")
            board_fen = fen_list[0]
            board = []

            for row in board_fen.split("/"):
                new_row = []
                count = 0

                for char in row:

                    if char.isnumeric():
                        count += int(char)

                    else:
                        if count > 0:
                            new_row.extend(["    " for _ in range(count)])
                            count = 0

                        if char in figures_map:
                            new_row.append(figures_map[char])

                        else:
                            raise ValueError("Invalid character found in FEN string: " + char)

                if count > 0:
                    new_row.extend(["    " for _ in range(count)])

                if len(new_row) != 8:
                    raise ValueError("Invalid number of figures in a row")

                board.append(new_row)

            try:
                move_turn, move_number = fen_list[1], fen_list[-1]

                print("Move Turn: ", move_turn)

                print("Move Number: ", move_number)
            except IndexError:
                print("No additional position info was provided")

            return board

        board = fen_parser(self.fen)

        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].append(board[i][j])

    def print_board(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.board[i][j][0] == 0:
                    termcolor.cprint(self.board[i][j][1], "grey", "on_white", end="")
                else:
                    termcolor.cprint(self.board[i][j][1], "grey", "on_grey", end="")
                if j == self.width - 1:
                    print("\n", end="")

fen_string = "r5rk/1p1q1p1p/8/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
print(f"Enter FEN string (Default: {fen_string}): ", end="")

new_fen = input()

if new_fen != "":
    fen_string = new_fen

test_board = ChessBoard(8, 8, fen_string)

test_board.print_board()
