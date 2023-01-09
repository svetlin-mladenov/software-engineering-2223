from __future__ import annotations
from chess_piece_type import ChessPieceType, ChessPieceGroup


class ChessPiece:
    pieces: dict[tuple[ChessPieceType, ChessPieceGroup], str] = {
        (ChessPieceType.PAWN, ChessPieceGroup.ANIMALS): "🐹",
        (ChessPieceType.ROOK, ChessPieceGroup.ANIMALS): "🐻",
        (ChessPieceType.KNIGHT, ChessPieceGroup.ANIMALS): "🐴",
        (ChessPieceType.BISHOP, ChessPieceGroup.ANIMALS): "🐼",
        (ChessPieceType.QUEEN, ChessPieceGroup.ANIMALS): "🦊",
        (ChessPieceType.KING, ChessPieceGroup.ANIMALS): "🦁",
        (ChessPieceType.EMPTY, ChessPieceGroup.ANIMALS): "  ",

        (ChessPieceType.PAWN, ChessPieceGroup.PLANTS): "🌱",
        (ChessPieceType.ROOK, ChessPieceGroup.PLANTS): "🌻",
        (ChessPieceType.KNIGHT, ChessPieceGroup.PLANTS): "🌾",
        (ChessPieceType.BISHOP, ChessPieceGroup.PLANTS): "🌷",
        (ChessPieceType.QUEEN, ChessPieceGroup.PLANTS): "🌹",
        (ChessPieceType.KING, ChessPieceGroup.PLANTS): "🌵",
        (ChessPieceType.EMPTY, ChessPieceGroup.PLANTS): "  ",

        (ChessPieceType.PAWN, ChessPieceGroup.CREATURES): "🧚",
        (ChessPieceType.ROOK, ChessPieceGroup.CREATURES): "🧙",
        (ChessPieceType.KNIGHT, ChessPieceGroup.CREATURES): "🧜",
        (ChessPieceType.BISHOP, ChessPieceGroup.CREATURES): "🧛",
        (ChessPieceType.QUEEN, ChessPieceGroup.CREATURES): "🧝",
        (ChessPieceType.KING, ChessPieceGroup.CREATURES): "🤴",
        (ChessPieceType.EMPTY, ChessPieceGroup.CREATURES): "  ",

        (ChessPieceType.PAWN, ChessPieceGroup.BIRDS): "🐥",
        (ChessPieceType.ROOK, ChessPieceGroup.BIRDS): "🦆",
        (ChessPieceType.KNIGHT, ChessPieceGroup.BIRDS): "🦅",
        (ChessPieceType.BISHOP, ChessPieceGroup.BIRDS): "🦩",
        (ChessPieceType.QUEEN, ChessPieceGroup.BIRDS): "🦉",
        (ChessPieceType.KING, ChessPieceGroup.BIRDS): "🦚",
        (ChessPieceType.EMPTY, ChessPieceGroup.BIRDS): "  ",

        (ChessPieceType.PAWN, ChessPieceGroup.FARM): "🦔",
        (ChessPieceType.ROOK, ChessPieceGroup.FARM): "🐷",
        (ChessPieceType.KNIGHT, ChessPieceGroup.FARM): "🐮",
        (ChessPieceType.BISHOP, ChessPieceGroup.FARM): "🐏",
        (ChessPieceType.QUEEN, ChessPieceGroup.FARM): "🐱",
        (ChessPieceType.KING, ChessPieceGroup.FARM): "🐶",
        (ChessPieceType.EMPTY, ChessPieceGroup.FARM): "  "
    }

    fen_map = {
        "p": ChessPieceType.PAWN,
        "r": ChessPieceType.ROOK,
        "n": ChessPieceType.KNIGHT,
        "b": ChessPieceType.BISHOP,
        "q": ChessPieceType.QUEEN,
        "k": ChessPieceType.KING,
    }

    def __init__(self, piece_type: ChessPieceType, group: ChessPieceGroup):
        self.emoji = ChessPiece.pieces[(piece_type, group)]
        self.piece_type = piece_type
        self.group = group

    def __str__(self):
        return self.emoji

    @staticmethod
    def from_fen(symbol: str, player_group: ChessPieceGroup, opponent_group: ChessPieceGroup) -> ChessPiece:
        return ChessPiece(ChessPiece.fen_map[symbol.lower()], opponent_group if symbol.islower() else player_group)
