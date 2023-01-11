package com.kris.chessProject.piece;

public class Bishop extends Piece {
    public Bishop(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'B' : 'b';
    }
}
