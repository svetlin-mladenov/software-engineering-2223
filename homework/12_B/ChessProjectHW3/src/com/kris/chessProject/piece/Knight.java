package com.kris.chessProject.piece;

public class Knight extends Piece {
    public Knight(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'N' : 'n';
    }
}
