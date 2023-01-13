from chess_piece_type import ChessPieceType, ChessPieceGroup
from chess_piece import ChessPiece


class ChessBoard:
    def __init__(self, player_group: ChessPieceGroup = ChessPieceGroup.ANIMALS, opponent_group: ChessPieceGroup = ChessPieceGroup.PLANTS):
        self.size = 8
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


if __name__ == "__main__":
    board = ChessBoard()
    print(board)
