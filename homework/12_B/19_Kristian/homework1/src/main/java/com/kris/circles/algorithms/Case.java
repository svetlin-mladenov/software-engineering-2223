package com.kris.circles.algorithms;

public enum Case {
  EQUAL("The circles have the same parameters"),
  B_IN_A("The second circle, contains itself in the first"),
  A_IN_B("The first circle, contains itself in the second"),
  INTERSECT("The circles intersect each other"),
  TOUCH("The circles touch each other"),
  NOT_TOUCH("The circles DO NOT touch each other");

  private final String label;

  private Case(String label) {
    this.label = label;
  }

  public String getLabel() {
    return label;
  }
}
