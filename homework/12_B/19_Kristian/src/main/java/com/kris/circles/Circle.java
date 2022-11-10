package com.kris.circles;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@RequiredArgsConstructor
@Getter
@Setter
@ToString
@EqualsAndHashCode
public class Circle {
  private final float x;
  private final float y;
  private final float r;
}
