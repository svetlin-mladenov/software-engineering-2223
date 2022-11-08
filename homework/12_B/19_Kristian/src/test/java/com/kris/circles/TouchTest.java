package com.kris.circles;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.kris.circles.algorithms.CircleAlgorithms;

class TouchTest {
  Circle first;
  Circle second;
  CircleAlgorithms alg;

  private final PrintStream standardOut = System.out;
  private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

  @BeforeEach
  public void setUp() throws Exception {
    System.setOut(new PrintStream(outputStreamCaptor));
  }

  @AfterEach
  void tearDown() throws Exception {
    System.setOut(standardOut);
  }

  @Test
  void succeed() {
    first = new Circle(0, 0, 2);
    second = new Circle(-4f, 0, 2);
    alg = new CircleAlgorithms(first, second);

    alg.run();
    assertEquals("The circles touch each other", outputStreamCaptor.toString().trim());
  }

  @Test
  void fail() {
    first = new Circle(0, 0, 2);
    second = new Circle(0, 0, 1);
    alg = new CircleAlgorithms(first, second);

    alg.run();
    assertNotEquals("The circles touch each other", outputStreamCaptor.toString().trim());
  }
}
