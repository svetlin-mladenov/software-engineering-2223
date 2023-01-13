package org.kris.chess.game.figures;

import org.kris.chess.game.Colors;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@ToString
@Getter
@Setter
@AllArgsConstructor
public abstract class AbstractFigure {
	private final Colors color;
	private int row;
	private char col;
	
	public void printFigure() {
		System.out.print(" ");
	}
	
	protected void moveWithPattern() {
		whereToMoveWithPattern();
		//soon
	}
	
	private void whereToMoveWithPattern() {
		//soon
	}
}
