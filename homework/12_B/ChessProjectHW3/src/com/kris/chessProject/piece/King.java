package com.kris.chessProject.piece;

public class King extends Piece {
    public King(Color color) {
        super(color);
    }

    @Override
    public char getSymbol() {
        return getColor() == Color.WHITE ? 'K' : 'k';
    }
}
