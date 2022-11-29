package com.kris.circles;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.kris.circles.algorithms.Case;
import com.kris.circles.algorithms.CircleAlgorithms;

class CircleAlgorithmsTest {
  Circle first;
  Circle second;
  CircleAlgorithms alg;

  private final PrintStream standardOut = System.out;
  private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

  @BeforeEach
  public void setUp() throws Exception {
    System.setOut(new PrintStream(outputStreamCaptor));
    alg = new CircleAlgorithms();
  }

  @AfterEach
  void tearDown() throws Exception {
    System.setOut(standardOut);
  }

  @Test
  void shouldAInBSucceed() {
    first = new Circle(-1, -1, 1);
    second = new Circle(1, 0, 10);

    assertEquals(alg.calculateDistance(first, second), Case.A_IN_B);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The first circle, contains itself in the second", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldAInBFail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 2, 1);

    assertNotEquals(alg.calculateDistance(first, second), Case.A_IN_B);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The first circle, contains itself in the second", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldBInASucceed() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 1);

    assertEquals(alg.calculateDistance(first, second), Case.B_IN_A);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The second circle, contains itself in the first", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldBInAFail() {
    first = new Circle(0, 0, 1);
    second = new Circle(0, 2, 2);

    assertNotEquals(alg.calculateDistance(first, second), Case.B_IN_A);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The second circle, contains itself in the first", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldEqualSucceed() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 2);

    assertEquals(alg.calculateDistance(first, second), Case.EQUAL);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The circles have the same parameters", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldEqualFail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 2, 2);

    assertNotEquals(alg.calculateDistance(first, second), Case.EQUAL);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The circles have the same parameters", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldIntersectSucceed() {
    first = new Circle(0, 0, 2);
    second = new Circle(-2.5f, 1, 2.5f);

    assertEquals(alg.calculateDistance(first, second), Case.INTERSECT);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The circles intersect each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldIntersectFail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 1);

    assertNotEquals(alg.calculateDistance(first, second), Case.INTERSECT);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The circles intersect each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldNotTouchSucceed() {
    first = new Circle(24.8f, 13.123f, 2);
    second = new Circle(-43.52f, -25.876f, 2);

    assertEquals(alg.calculateDistance(first, second), Case.NOT_TOUCH);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The circles DO NOT touch each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldNotTouchFail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 2);

    assertNotEquals(alg.calculateDistance(first, second), Case.NOT_TOUCH);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The circles DO NOT touch each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldTouchSucceed() {
    first = new Circle(0, 0, 2);
    second = new Circle(-4f, 0, 2);

    assertEquals(alg.calculateDistance(first, second), Case.TOUCH);

    System.out.println(alg.printEnum(first, second));
    assertEquals("The circles touch each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void shouldTouchFail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 1);

    assertNotEquals(alg.calculateDistance(first, second), Case.TOUCH);

    System.out.println(alg.printEnum(first, second));
    assertNotEquals("The circles touch each other", outputStreamCaptor.toString().trim());
  }
}
