package circle;

import java.awt.Point;
import java.util.ArrayList;

public class GetCoords {
	public static int[] fX = new int[1600];
	public static int[] fY = new int[1600];
	public static int width = 8;
	public static double[] cW = new double[3];
	public static ArrayList<Point> CoordsList = new ArrayList<Point>();

	
	public static void main(String[] args) {
		getCoords();
		changeZeros();
		for(int i=0;i<1600;i++) {
			if(fX[i] <10 && fY[i] < 10) {
				System.out.println("(" + fX[i] + ", " + fY[i] + ")");
			}
		}
		System.out.println("\n\n\n");
		for(int i=0;i<CoordsList.size();i++) {
			System.out.println("(" + (int)CoordsList.get(i).getX() + ", " + (int)CoordsList.get(i).getY() + ")");

		}
	}
	
	public static void changeZeros() {
		for(int i=0;i<1600;i++) {
			int[] coordTotal = new int[1600];
			coordTotal[i] = fX[i] + fY[i];
			if(coordTotal [i] == 0) {
				fX[i] = 1600;
				fY[i] = 1600;
			}
		}
	}
	
	public static void getCoords() {
		fX[0] = width;
		fY[0] = 0;
		int x = width;
		int y = 0;
		int i = 1;

		while(!(x == 0 && y == width)) {
			
			cW[0] = Math.abs(width-Math.sqrt((x-1)*(x-1) + (y+1)*(y+1)));
			cW[1] = Math.abs(width-Math.sqrt((x)*(x) + (y+1)*(y+1)));
			cW[2] = Math.abs(width-Math.sqrt((x-1)*(x-1) + (y)*(y)));
			
			if(cW[0]<cW[1] && cW[0]<cW[2]) {
				fX[i] = (int) (x-1);
				fY[i] = (int) (y+1);
				CoordsList.add(new Point(x-1,y+1));

				x = x-1;
				y = y+1;
			}
			else if(cW[1]<cW[0] && cW[1]<cW[2]) {
				fX[i] = (int) (x);
				fY[i] = (int) (y+1);
				CoordsList.add(new Point(x,y+1));

				y = y+1;
			}
			else if(cW[2]<cW[0] && cW[2]<cW[1]) {
				fX[i] = (int) (x-1);
				fY[i] = (int) (y);
				CoordsList.add(new Point(x-1,y));

				x = x-1;
			}
			i++;
		}
	}
}
