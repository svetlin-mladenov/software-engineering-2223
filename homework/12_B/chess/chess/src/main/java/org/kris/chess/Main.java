package org.kris.chess;

import org.kris.chess.game.Board;

public class Main {

	public static void main(String[] args) {
		Board chess = new Board();
		
		chess.printBoard();
		chess.printFiguresInfo();
	}

}
