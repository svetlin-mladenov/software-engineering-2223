import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MainTest {

    @Test
    void crossing() {
        assertEquals(OverlayType.CROSSING, Main.crossType(
                new Circle(new Point(0, 0), 2),
                new Circle(new Point(2, 2), 1)));

        assertEquals(OverlayType.CROSSING, Main.crossType(
                new Circle(new Point(5.5, 8), 12),
                new Circle(new Point(1, -1.5), 9.8)));
    }

    @Test
    void notCrossing() {
        assertEquals(OverlayType.NOT_CROSSING, Main.crossType(
                new Circle(new Point(20, 40), 5),
                new Circle(new Point(-70, 0), 8)));

        assertEquals(OverlayType.NOT_CROSSING, Main.crossType(
                new Circle(new Point(0, 0), 5),
                new Circle(new Point(7, 7), 0.1)));
    }

    @Test
    void identical() {
        assertEquals(OverlayType.IDENTICAL, Main.crossType(
                new Circle(new Point(5, 5), 5.865),
                new Circle(new Point(5, 5), 5.865)));

        assertEquals(OverlayType.IDENTICAL, Main.crossType(
                new Circle(new Point(0, 0), 30),
                new Circle(new Point(0, 0), 30)));
    }


    @Test
    void touching() {
        assertEquals(OverlayType.TOUCHING, Main.crossType(
                new Circle(new Point(10, 10), 5),
                new Circle(new Point(10, 0), 5)));

        assertEquals(OverlayType.TOUCHING, Main.crossType(
                new Circle(new Point(0, 4), 1),
                new Circle(new Point(0, 0), 3)));
    }


    @Test
    void one_inside_other() {
        assertEquals(OverlayType.ONE_INSIDE_OTHER, Main.crossType(
                new Circle(new Point(0, 0), 5),
                new Circle(new Point(0, 0), 50)));

        assertEquals(OverlayType.ONE_INSIDE_OTHER, Main.crossType(
                new Circle(new Point(4, 8), 3.333),
                new Circle(new Point(7, 7), 500.97)));
    }
}