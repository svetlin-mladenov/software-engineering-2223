package com.kris.chessProject.piece;

public class Queen extends Piece {
    public Queen(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'Q' : 'q';
    }
}
