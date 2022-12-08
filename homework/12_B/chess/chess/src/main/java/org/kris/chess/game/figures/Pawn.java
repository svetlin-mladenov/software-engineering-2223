package org.kris.chess.game.figures;

import org.kris.chess.game.Colors;

import lombok.ToString;

@ToString(callSuper = true)
public class Pawn extends AbstractFigure {

	public Pawn(Colors color, int row, char col) {
		super(color, row, col);
	}

	@Override
	public void printFigure() {
		if(getColor() == Colors.WHITE) {
			System.out.print("♙");			
		}
		else if(getColor() == Colors.BLACK) {
			System.out.print("♟");			
		}
	}
}
