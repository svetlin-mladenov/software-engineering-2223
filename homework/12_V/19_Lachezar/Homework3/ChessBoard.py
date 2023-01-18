from dataclasses import dataclass
import typing

@dataclass
class ChessBoard:
    notation: str

    def map_fen_character(self, char: str) -> str:
        if char.isnumeric():
            return [" "] * int(char)
        switch={
            'p': '♟︎',
            'r': '♜',
            'n': '♞',
            'k': '♚',
            'q': '♛',
            'b': '♝',

            'P': '♙',
            'R': '♖',
            'N': '♘',
            'K': '♔',
            'Q': '♕',
            'B': '♗',
        }
        return switch.get(char, "")
    
    def get_board_str_value(self) -> list[str]:
        board_pieces_list = list(map(self.map_fen_character, list(self.notation.split(' ', maxsplit=1)[0].replace("/", "").replace(" ", ""))))
        sanitised_pieces_list = []
        for piece in board_pieces_list:
            if type(piece) == type([]):
                sanitised_pieces_list.extend(piece)
            else:
                sanitised_pieces_list.append(piece)
        return sanitised_pieces_list
    def print(self):
        board = """
            ┌────┬────┬────┬────┬────┬────┬────┬────┐
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            ├────┼────┼────┼────┼────┼────┼────┼────┤
            | {}  | {}  | {}  | {}  | {}  | {}  | {}  | {}  |
            └────┴────┴────┴────┴────┴────┴────┴────┘
        """
        board_val = self.get_board_str_value()
        if len(board_val) != 64:
            print("Notation is incorrect")
            return
        print("Board position")
        print(self.notation)
        print(board.format(*board_val))


ChessBoard("rbqkb3/pp1pBp1p/6p1/4p1n1/n7/2K3r1/PP1PPPPP/R3BRNN b - - 0 1").print()
ChessBoard("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25").print()
