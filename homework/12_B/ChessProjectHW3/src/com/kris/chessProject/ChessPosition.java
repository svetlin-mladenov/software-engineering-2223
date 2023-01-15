package com.kris.chessProject;

import java.util.Arrays;

import com.kris.chessProject.piece.Bishop;
import com.kris.chessProject.piece.King;
import com.kris.chessProject.piece.Knight;
import com.kris.chessProject.piece.Pawn;
import com.kris.chessProject.piece.Piece;
import com.kris.chessProject.piece.Piece.Color;
import com.kris.chessProject.piece.Queen;
import com.kris.chessProject.piece.Rook;

public class ChessPosition {
	public Piece[][] board;
	public boolean whiteToMove;
	public boolean canWhiteCastleKingside;
	public boolean canWhiteCastleQueenside;
	public boolean canBlackCastleKingside;
	public boolean canBlackCastleQueenside;
	public int enPassantColumn;
	public int halfMoveClock;
	public int fullMoveNumber;

	@SuppressWarnings("unused")
	public ChessPosition() {
		board = new Piece[8][8];
		
		if(false) {
			initStartBoard();
		}
		
		whiteToMove = true;
		canWhiteCastleKingside = true;
		canWhiteCastleQueenside = true;
		canBlackCastleKingside = true;
		canBlackCastleQueenside = true;
		enPassantColumn = -1;
		halfMoveClock = 0;
		fullMoveNumber = 1;
	}
	
	//That is func for initing the board, but in our case we do not need it now because we parseFEN directly to the board
	private void initStartBoard() {
		board[0] = new Piece[] { new Rook(Color.BLACK), new Knight(Color.BLACK), new Bishop(Color.BLACK),
				new Queen(Color.BLACK), new King(Color.BLACK), new Bishop(Color.BLACK), new Knight(Color.BLACK),
				new Rook(Color.BLACK) };
		board[1] = new Piece[] { new Pawn(Color.BLACK), new Pawn(Color.BLACK), new Pawn(Color.BLACK),
				new Pawn(Color.BLACK), new Pawn(Color.BLACK), new Pawn(Color.BLACK), new Pawn(Color.BLACK),
				new Pawn(Color.BLACK) };
		for (int i = 2; i < 6; i++) {
			Arrays.fill(board[i], null);
		}
		board[6] = new Piece[] { new Pawn(Color.WHITE), new Pawn(Color.WHITE), new Pawn(Color.WHITE),
				new Pawn(Color.WHITE), new Pawn(Color.WHITE), new Pawn(Color.WHITE), new Pawn(Color.WHITE),
				new Pawn(Color.WHITE) };
		board[7] = new Piece[] { new Rook(Color.WHITE), new Knight(Color.WHITE), new Bishop(Color.WHITE),
				new Queen(Color.WHITE), new King(Color.WHITE), new Bishop(Color.WHITE), new Knight(Color.WHITE),
				new Rook(Color.WHITE) };
	}

	public static ChessPosition parseFEN(String fen) {
	    ChessPosition position = new ChessPosition();

	    String[] parts = fen.split(" ");
	    String[] rows = parts[0].split("/");
	    for (int i = rows.length - 1; i >= 0; i--) {
	        int column = 0;
	        for (int j = 0; j < rows[i].length(); j++) {
	            char c = rows[i].charAt(j);
	            if (c >= '1' && c <= '8') {
	                column += c - '0';
	            } else {
	                Piece.Color color = Character.isUpperCase(c) ? Piece.Color.WHITE : Piece.Color.BLACK;
	                position.board[7 - i][column] = parsePiece(Character.toLowerCase(c), color);
	                column++;
	            }
	        }
	    }

	    position.whiteToMove = parts[1].equals("w");
	    position.canWhiteCastleKingside = parts[2].contains("K");
	    position.canWhiteCastleQueenside = parts[2].contains("Q");
	    position.canBlackCastleKingside = parts[2].contains("k");
	    position.canBlackCastleQueenside = parts[2].contains("q");
	    if (!parts[3].equals("-")) {
	        position.enPassantColumn = parts[3].charAt(0) - 'a';
	    }
	    position.halfMoveClock = Integer.parseInt(parts[4]);
	    position.fullMoveNumber = Integer.parseInt(parts[5]);

	    return position;
	}

	private static Piece parsePiece(char c, Color color) {
	    switch (c) {
	        case 'p':
	            return new Pawn(color);
	        case 'r':
	            return new Rook(color);
	        case 'n':
	            return new Knight(color);
	        case 'b':
	            return new Bishop(color);
	        case 'q':
	            return new Queen(color);
	        case 'k':
	            return new King(color);
	        default:
	            throw new IllegalArgumentException("Invalid piece type: " + c);
	    }
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (int i = 7; i >= 0; i--) {
			for (int j = 0; j < 8; j++) {
				Piece p = board[i][j];
				sb.append(p == null ? '.' : p.getSymbol());
			}
			sb.append('\n');
		}
		return sb.toString();
	}
}
