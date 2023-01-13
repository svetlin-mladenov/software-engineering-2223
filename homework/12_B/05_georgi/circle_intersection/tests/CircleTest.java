import org.junit.Before;
import org.junit.Test;

import static java.lang.Math.sqrt;
import static org.junit.Assert.*;

public class CircleTest {
    Circle circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8;

    @Before
    public void setUp()
    {
        circle1 = new Circle(2.0, 3.0, 12.0);
        circle2 = new Circle(15.0, 28.0, 10.0);

        circle3 = new Circle(2.0, 1.0, sqrt(5));
        circle4 = new Circle(4.0, 5.0, 3*sqrt(5));

        circle5 = new Circle(1.0, 1.0, 5.0);
        circle6 = new Circle(11.0, 1.0, 5.0);

        circle7 = new Circle(1.0, 1.0, 5.0);
        circle8 = new Circle(1.0, 1.0, 5.0);
    }

    @Test
    public void circle_intersection1() {
        assertEquals("The circles do not intersect.", circle1.circle_intersection(circle2));
    }
    @Test
    public void circle_intersection2() {
        assertEquals("Circles intersect at two points.", circle3.circle_intersection(circle4));
    }
    @Test
    public void circle_intersection3() {
        assertEquals("Circles intersect at one point.", circle5.circle_intersection(circle6));
    }
    @Test
    public void circle_intersection4() {
        assertEquals("The circles are the same.", circle7.circle_intersection(circle8));
    }
}