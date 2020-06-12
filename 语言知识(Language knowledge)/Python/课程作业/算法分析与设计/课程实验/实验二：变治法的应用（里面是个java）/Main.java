import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Point {
    double x;
    double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}
public class Main {
    static Point[] point;
    static double[] s = new double[6];
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
    	System.out.println("1111111");
        int n = in.nextInt();
        point = new Point[n];
//        for (int i = 0; i < n; i++) {
//            int a = in.nextInt();
//            int b = in.nextInt();
//            point[i] = new Point(a, b);
//        }
        point[0] = new Point(3,15);
        point[1] = new Point(8,3);
        point[2] = new Point(15,15);
        point[3] = new Point(8,30);
        point[4] = new Point(4,16);
        point[5] = new Point(8,15);
        Arrays.sort(point,0, n, new Comparator<Point>() {
            public int compare(Point o1, Point o2) {
                if (o1.x - o2.x == 0) {
                    return (int) (o1.y - o2.y);
                }
                return (int) (o1.x - o2.x);
            }
        });
        System.out.println(point[0].x + "," + point[0].y);
        hull(1, n-1,point[0],point[0]);
    }

    private static void hull(int l,int r,Point p1,Point p2){
        int x=l;
        int i=l-1,j=r+1;
        /**
         * 找出距离直线p1-p2最远的点p3
         * */
        for (int k = l; k <= r; k++){
            if (s[x] - s[k] <= 0) {
                x=k;
            }
        }
        Point p3 = point[x];
        /**
         * p1-p3左侧的点
         * */
        for (int k = l; k <= r; k++) {

            s[++i] = cross(point[k], p1, p3);
            if (s[i] > 0) {
                Point temp = point[i];
                point[i] = point[k];
                point[k] = temp;
            } else {
                i--;
            }
        }
        /**
         * 直线p3-p2右侧的点
         * */
        for (int k=r;k>=l;k--) {
            s[--j]=cross(point[k], p3, p2);
            if (s[j] > 0) {
                Point temp = point[j];
                point[j] = point[k];
                point[k] = temp;
            } else {
                j++;
            }
        }
        /**
         * 分治，并中序输出
         * */
        if (l <= i) {
            hull(l, i, p1, p3);
        }
        System.out.println(p3.x + "," + p3.y);
        if (j <= r) {
            hull(j, r, p3, p2);
        }
    }
    private static double cross (Point a, Point b, Point c) {
        return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
    }
}
