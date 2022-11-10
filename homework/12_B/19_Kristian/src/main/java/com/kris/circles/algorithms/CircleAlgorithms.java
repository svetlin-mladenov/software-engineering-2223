package com.kris.circles.algorithms;

import com.kris.circles.Circle;

public class CircleAlgorithms {

	public String printEnum(Circle circle1, Circle circle2) {
		return calculateDistance(circle1, circle2).getLabel();
	}
	
	public Case calculateDistance(Circle circle1, Circle circle2) {
		return getCase(circle1, circle2);
	}

	private Case getCase(Circle circle1, Circle circle2) {
		if (circle1.equals(circle2)) {
			return Case.EQUAL;
		}
		
		double sideX = Math.abs(circle1.getX() - circle2.getX());
		double sideY = Math.abs(circle1.getY() - circle2.getY());
		double distance = Math.hypot(sideX, sideY);

		if (distance <= circle1.getR() - circle2.getR()) {
			return Case.B_IN_A;
		}
		if (distance <= circle2.getR() - circle1.getR()) {
			return Case.A_IN_B;
		}
		if (distance < circle1.getR() + circle2.getR()) {
			return Case.INTERSECT;
		}
		if (distance == circle1.getR() + circle2.getR()) {
			return Case.TOUCH;
		}

		return Case.NOT_TOUCH;
	}
}
