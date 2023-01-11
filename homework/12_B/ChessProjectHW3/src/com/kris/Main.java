package com.kris;

import com.kris.chessProject.ChessPosition;

public class Main {

	public static void main(String[] args) {
		String fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25";
	    ChessPosition position = ChessPosition.parseFEN(fen);
	    System.out.println(position);
	}
}
