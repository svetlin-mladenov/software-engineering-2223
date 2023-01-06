package com.kris.chessProject.piece;

public class Rook extends Piece {
    public Rook(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'R' : 'r';
    }
}
