package com.kris.chessProject.piece;

public class Pawn extends Piece {
    public Pawn(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'P' : 'p';
    }
}
