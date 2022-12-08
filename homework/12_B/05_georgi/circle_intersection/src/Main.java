import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        Circle circle1 = new Circle(2.0, 3.0, 12.0);
        Circle circle2 = new Circle(15.0, 28.0, 10.0);

        circle1.circle_intersection(circle2);//no intersect

        Circle circle3 = new Circle(2.0, 1.0, sqrt(5));
        Circle circle4 = new Circle(4.0, 5.0, 3*sqrt(5));

        circle3.circle_intersection(circle4);//intersect at 2 points

        Circle circle5 = new Circle(1.0, 1.0, 5.0);
        Circle circle6 = new Circle(11.0, 1.0, 5.0);

        circle5.circle_intersection(circle6);//intersect at 1 points

        Circle circle7 = new Circle(1.0, 1.0, 5.0);
        Circle circle8 = new Circle(1.0, 1.0, 5.0);
        circle7.circle_intersection(circle8);//same circles
        System.out.println(circle7.d);
        System.out.println(circle7.getR());
        System.out.println(circle8.getR());

    }
}
