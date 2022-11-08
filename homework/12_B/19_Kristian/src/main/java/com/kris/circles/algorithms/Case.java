package com.kris.circles.algorithms;

public enum Case {
  EQUAL("The circles have the same parameters"),
  BINA("The second circle, contains itself in the first"),
  AINB("The first circle, contains itself in the second"),
  INTERSECT("The circles intersect each other"),
  TOUCH("The circles touch each other"),
  NOTTOUCH("The circles DO NOT touch each other");
  
  private final String label;

  private Case(String label) {
    this.label = label;
  }

  public String getLabel() {
    return label;
  }
}