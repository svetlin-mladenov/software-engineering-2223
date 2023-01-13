public class Circle {
    private Point center;
    private double r;

    Circle(Point center, double radius) {
        this.center = center;
        this.r = radius;
    }

    public Point getCenter() {
        return center;
    }

    public void setCenter(Point center) {
        this.center = center;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }

    public boolean equals(Circle other) {
        if (this.r == other.getR()) {
            if (this.center.getX() == other.center.getX()) {
                if (this.center.getY() == other.center.getY()) {
                    return true;
                }
            }
        }
        return false;
    }
}
