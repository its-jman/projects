package circle;

import java.awt.Point;
import java.util.ArrayList;

public class MakeCircle {
	public static int radius = 8;
	public static ArrayList<Point> CoordsList = new ArrayList<Point>();
	
	public static void main(String[] args) {
		//CoordsList.add(new Point(radius,0));
		//CoordsList.add(new Point(radius, 1)); //THIS LINE SHOULD NOT HAVE TO BE HERE, but it does...
		
		
		MakeQuarterCircle();
		//CoordsList.remove(CoordsList.size()-1);
		PrintCoordsList();
	}
	
	public static void PrintCoordsList() {
		for(int i=0;i<CoordsList.size();i++) {
			System.out.println("(" + CoordsList.get(i).getX() + ", " + CoordsList.get(i).getY() + ")");
		}
	}
	
	public static void MakeQuarterCircle() {
		int x = radius;
		int y = 0;
		double[] cW = new double[3];
		
		while(!(x == 0 && y == radius)) {
			
			cW[0] = Math.abs(radius-(Math.sqrt((x-1)*(x-1) + (y+1)*(y+1))));
			cW[1] = Math.abs(radius-(Math.sqrt((x)*(x) + (y+1)*(y+1))));
			cW[2] = Math.abs(radius-(Math.sqrt((x-1)*(x-1) + (y)*(y))));
				
			if(cW[0]<cW[1] && cW[0]<cW[2]) {
				CoordsList.add(new Point(x-1,y+1));			

				x = x-1;
				y = y+1;
			}
			else if(cW[1]<cW[0] && cW[1]<cW[2]) {
				CoordsList.add(new Point(x,y+1));

				y = y+1;
			}
			else if(cW[2]<cW[0] && cW[2]<cW[1]) {
				CoordsList.add(new Point(x-1,y));

				x = x-1;
			}
		}
	}
}
