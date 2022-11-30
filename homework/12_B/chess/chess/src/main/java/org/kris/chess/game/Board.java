package org.kris.chess.game;

import org.kris.chess.game.figures.AbstractFigure;
import org.kris.chess.game.figures.Bishop;
import org.kris.chess.game.figures.King;
import org.kris.chess.game.figures.Knight;
import org.kris.chess.game.figures.Pawn;
import org.kris.chess.game.figures.Queen;
import org.kris.chess.game.figures.Rook;

public class Board {
	private AbstractFigure[][] board;
//	private AbstractFigure[] takenWhite;
//	private AbstractFigure[] takenBlack;

	public Board() {
		board = new AbstractFigure[8][8];
		initBoard();
//		takenBlack = new AbstractFigure[16];
//		takenWhite = new AbstractFigure[16];
	}

	private void initBoard() {
		for (int i = 0; i < 8; i++) {
			AbstractFigure tempWPawn = new Pawn(Colors.WHITE, 2, (char) ('A' + i));
			AbstractFigure tempBPawn = new Pawn(Colors.BLACK, 7, (char) ('A' + i));

			board[i][1] = tempWPawn;
			board[i][6] = tempBPawn;
		}
		AbstractFigure wRook1 = new Rook(Colors.WHITE, 1, 'A');
		AbstractFigure wRook2 = new Rook(Colors.WHITE, 1, 'H');
		AbstractFigure wKnight1 = new Knight(Colors.WHITE, 1, 'B');
		AbstractFigure wKnight2 = new Knight(Colors.WHITE, 1, 'G');
		AbstractFigure wBishop1 = new Bishop(Colors.WHITE, 1, 'C');
		AbstractFigure wBishop2 = new Bishop(Colors.WHITE, 1, 'F');
		AbstractFigure wQueen = new Queen(Colors.WHITE, 1, 'D');
		AbstractFigure wKing = new King(Colors.WHITE, 1, 'E');

		AbstractFigure bRook1 = new Rook(Colors.BLACK, 8, 'A');
		AbstractFigure bRook2 = new Rook(Colors.BLACK, 8, 'H');
		AbstractFigure bKnight1 = new Knight(Colors.BLACK, 8, 'B');
		AbstractFigure bKnight2 = new Knight(Colors.BLACK, 8, 'G');
		AbstractFigure bBishop1 = new Bishop(Colors.BLACK, 8, 'C');
		AbstractFigure bBishop2 = new Bishop(Colors.BLACK, 8, 'F');
		AbstractFigure bQueen = new Queen(Colors.BLACK, 8, 'D');
		AbstractFigure bKing = new King(Colors.BLACK, 8, 'E');

		board[0][0] = wRook1;
		board[7][0] = wRook2;
		board[1][0] = wKnight1;
		board[6][0] = wKnight2;
		board[2][0] = wBishop1;
		board[5][0] = wBishop2;
		board[3][0] = wQueen;
		board[4][0] = wKing;

		board[0][7] = bRook1;
		board[7][7] = bRook2;
		board[1][7] = bKnight1;
		board[6][7] = bKnight2;
		board[2][7] = bBishop1;
		board[5][7] = bBishop2;
		board[3][7] = bQueen;
		board[4][7] = bKing;
	}

	public void printBoard() {
		System.out.println("            a        b       c       d       e       f       g       h");

		System.out.println("  ------------------------------------------------------------------------");
		int count = 8;
		for (int i = 7; i >= 0; i--) {
			System.out.print(count + "\t");
			System.out.print("|\t");
			for (int j = 0; j < 8; j++) {
				if (board[j][i] == null) {
					System.out.print(" |\t");
				} else {
					board[j][i].printFigure();
					System.out.print("|\t");
				}
			}
			System.out.print(count);
			count--;
			System.out.println();
			System.out.println("  ------------------------------------------------------------------------");
		}
		System.out.println("            a        b       c       d       e       f       g       h");
		System.out.println("\n\n");
	}
	
	public void printFiguresInfo() {
		for (int i = 7; i >= 0; i--) {
			for (int j = 0; j < 8; j++) {
					if(board[j][i] != null) {
						System.out.println(board[j][i].toString());
					}
				}
			}
	}

	public void changeFigPos() {
		// soon
	}

	public void addInTaken() {
		// soon
	}
}
