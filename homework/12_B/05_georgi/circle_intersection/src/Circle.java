import java.util.Objects;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

public class Circle {
    //centre
    Double x;
    Double y;
    //radius
    Double r;
    String result;
    Double d;

    public Circle(Double x, Double y, Double r) {
        this.x = x;
        this.y = y;
        this.r = r;
    }

    public Double getX() {
        return x;
    }

    public Double getY() {
        return y;
    }

    public Double getR() {
        return r;
    }

    String circle_intersection(Circle circle)
    {
        d = sqrt(pow(circle.getX() - this.x, 2) + pow(circle.getY() - this.y, 2));
        //intersects
        if(d == this.r + circle.getR())
        {
            result = "Circles intersect at one point.";
        }
        else if(this.r - circle.getR() < d && d < this.r + circle.getR())
        {
            result = "Circles intersect at two points.";
        }
        else if(d == this.r || d == circle.getR())
        {
            result = "The centre of one of the circles lies on the other circle.";
        }
        //number of intersections

        //the clash
        else if(Objects.equals(this.x, circle.getX()) && Objects.equals(this.y, circle.getY()) && Objects.equals(this.r, circle.getR()))
        {
            result = "The circles are the same.";
        }

        else
        {
            result = "The circles do not intersect.";
        }
        System.out.println(result);
        return result;
    }
}
