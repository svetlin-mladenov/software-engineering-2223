import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static OverlayType crossType(Circle c1, Circle c2) {
        if (c1.equals(c2)) {
            return OverlayType.IDENTICAL;
        }

        double distanceBtwCenters = Math.sqrt(
                Math.pow(c1.getCenter().getX() - c2.getCenter().getX(), 2) +
                        Math.pow(c1.getCenter().getY() - c2.getCenter().getY(), 2)
        );
        //System.out.println("distanceBtwCenters =  " + distanceBtwCenters);

        if (c1.getR() + c2.getR() == distanceBtwCenters) {
            return OverlayType.TOUCHING;
        }

        if ( (c1.getR() > c2.getR() && (distanceBtwCenters + c2.getR() <= c1.getR())) ||
                c2.getR() > c1.getR() && (distanceBtwCenters + c1.getR() <= c2.getR())) {
            return OverlayType.ONE_INSIDE_OTHER;
        }

        if (c1.getR() + c2.getR() > distanceBtwCenters) {
            return OverlayType.CROSSING;
        }

        if (c1.getR() + c2.getR() < distanceBtwCenters) {
            return OverlayType.NOT_CROSSING;
        }

        return null;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter radius, x and y for circle 1: ");
        Circle c1 = new Circle(new Point(in.nextDouble(), in.nextDouble()), in.nextDouble());

        System.out.println("Enter radius, x and y for circle 2: ");
        Circle c2 = new Circle(new Point(in.nextDouble(), in.nextDouble()), in.nextDouble());

        System.out.println(crossType(c1, c2));
    }
}