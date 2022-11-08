package com.kris.circles.algorithms;

import com.kris.circles.Circle;

public class CircleAlgorithms {
  private Circle firstCircle;
  private Circle secondCircle;

  public CircleAlgorithms(Circle one, Circle two) {
    firstCircle = one;
    secondCircle = two;
  }

  public void run() {
    System.out.println(calculate());
  }

  private String calculate() {
    double distance = Math.sqrt(Math.pow(Math.abs(firstCircle.getX() - Math.abs(secondCircle.getX())), 2)
        + Math.pow(Math.abs(firstCircle.getY() - Math.abs(secondCircle.getY())), 2));

    return returnCase(distance).getLabel();
  }

  private Case returnCase(double d) {
    if (firstCircle.getX() == secondCircle.getX() && firstCircle.getY() == secondCircle.getY()
        && firstCircle.getR() == secondCircle.getR()) {
      return Case.EQUAL;
    }
    if (d <= firstCircle.getR() - secondCircle.getR()) {
      return Case.BINA;
    }
    if (d <= secondCircle.getR() - firstCircle.getR()) {
      return Case.AINB;
    }
    if (d < firstCircle.getR() + secondCircle.getR()) {
      return Case.INTERSECT;
    }
    if (d == firstCircle.getR() + secondCircle.getR()) {
      return Case.TOUCH;
    }

    return Case.NOTTOUCH;
  }
}
