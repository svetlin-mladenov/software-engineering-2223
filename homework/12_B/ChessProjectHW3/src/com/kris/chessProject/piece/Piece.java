package com.kris.chessProject.piece;

public abstract class Piece {
	public enum Color { WHITE, BLACK }

    private Color color;

    public Piece(Color color) {
        this.color = color;
    }

    public Color getColor() {
        return color;
    }

    public abstract char getSymbol();

    @Override
    public String toString() {
        return Character.toString(getSymbol());
    }
}
