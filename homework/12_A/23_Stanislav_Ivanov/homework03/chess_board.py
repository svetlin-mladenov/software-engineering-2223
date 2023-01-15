from __future__ import annotations
from sys import argv
from chess_piece_type import ChessPieceType, ChessPieceGroup
from chess_piece import ChessPiece


class ChessBoard:
    size = 8
    
    def __init__(self, player_group: ChessPieceGroup = ChessPieceGroup.ANIMALS, opponent_group: ChessPieceGroup = ChessPieceGroup.PLANTS):
        self.board = [[ChessPiece(ChessPieceType.EMPTY, ChessPieceGroup.ANIMALS) for _ in range(self.size)] for _ in range(self.size - 4)]
        self.board.insert(0, [ChessPiece(ChessPieceType.PAWN, opponent_group) for _ in range(self.size)])
        self.board.append([ChessPiece(ChessPieceType.PAWN, player_group) for _ in range(self.size)])
        self.board.insert(0, [
            ChessPiece(ChessPieceType.ROOK, opponent_group),
            ChessPiece(ChessPieceType.KNIGHT, opponent_group),
            ChessPiece(ChessPieceType.BISHOP, opponent_group),
            ChessPiece(ChessPieceType.QUEEN, opponent_group),
            ChessPiece(ChessPieceType.KING, opponent_group),
            ChessPiece(ChessPieceType.BISHOP, opponent_group),
            ChessPiece(ChessPieceType.KNIGHT, opponent_group),
            ChessPiece(ChessPieceType.ROOK, opponent_group)
        ])
        self.board.append([
            ChessPiece(ChessPieceType.ROOK, player_group),
            ChessPiece(ChessPieceType.KNIGHT, player_group),
            ChessPiece(ChessPieceType.BISHOP, player_group),
            ChessPiece(ChessPieceType.QUEEN, player_group),
            ChessPiece(ChessPieceType.KING, player_group),
            ChessPiece(ChessPieceType.BISHOP, player_group),
            ChessPiece(ChessPieceType.KNIGHT, player_group),
            ChessPiece(ChessPieceType.ROOK, player_group)
        ])

    def __str__(self):
        result = "\n"
        for x, row in enumerate(self.board):
            result += f"\033[1m{8-x}\033[0m "
            for y, piece in enumerate(row):
                result += f"\033[{47-((x+y)%2)*7}m {piece} \033[0m"
            result += "\n"
        return result + "    \033[1m" + "   ".join([chr(ord("A") + i) for i in range(self.size)]) + "\033[0m"

    @staticmethod
    def from_fen(fen: str, player_group: ChessPieceGroup = ChessPieceGroup.ANIMALS, opponent_group: ChessPieceGroup = ChessPieceGroup.PLANTS) -> ChessBoard:
        board = []
        for segment in fen.split(" ")[0].split("/"):
            row = []
            for symbol in segment:
                if symbol.isdigit():
                    row.extend([ChessPiece(ChessPieceType.EMPTY, ChessPieceGroup.ANIMALS) for _ in range(int(symbol))])
                else:
                    row.append(ChessPiece.from_fen(symbol, player_group, opponent_group))
            board.append(row)
        chess_board = ChessBoard.__new__(ChessBoard)
        chess_board.board = board
        return chess_board


if __name__ == "__main__":
    if len(argv) > 2:
        print("Usage: python chess_board.py <FEN>")
        print("(for example: python chess_board.py \"r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25\")")
        exit(1)
    
    fen = argv[1] if len(argv) == 2 else input("Enter FEN: ")
    board = ChessBoard.from_fen(fen)
    print(board)
