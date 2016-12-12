package circle;

import java.awt.Point;
import java.util.ArrayList;
import java.util.Scanner;

public class GetStuffArrayList {
	public static ArrayList<Point> CoordsList = new ArrayList<Point>();
	public static ArrayList<Point> FullCoordsList = new ArrayList<Point>();

	public static ArrayList<String> lineType = new ArrayList<String>();
	public static int radius;
	private static Scanner s = new Scanner(System.in);
	public static ArrayList<Integer> lineTotals = new ArrayList<Integer>();
	
	
	public static void main(String[] args) {
		System.out.print("Enter the radius of the circle: ");
		while(radius <= 0) {
			//This needs to keep running until user inputs an integer > 0
			try {
				radius = Integer.parseInt(s.nextLine());
				if(radius <= 0) {
					throw new /*Does IllegalArgumentExcption work for this?*/ IllegalArgumentException("Integer must be greater than 0.");
				}
			}
			catch(NumberFormatException e) {
				System.out.print("Enter the radius (int > 0): ");
			}
			catch(IllegalArgumentException f) {
				System.out.print("Enter the radius (int > 0): ");
			}
		}
		
		lineTotals.add(1);
		lineType.add("point");
		CoordsList.add(new Point(radius,0));
		
		
		getQuarterCircle();
		printLineTotals();
		getFullCircle();
		printFullCirTotals();
	}
	
	public static void printLineTotals() {
		System.out.println("");
		for(int i=0;i<lineTotals.size();i++) {
			System.out.print(lineTotals.get(i) + " block long " + lineType.get(i) + "\n");
		}
		for(int i=0;i<CoordsList.size();i++) {
			System.out.print("\n(" + (int)CoordsList.get(i).getX() + ", " + (int)CoordsList.get(i).getY() + ")");
		}
	}
	
	public static void printFullCirTotals() {
		System.out.println("\n\n\n");
		for(int i=0;i<FullCoordsList.size();i++) {
			System.out.println("(" + (int)FullCoordsList.get(i).getX() + ", " + (int)FullCoordsList.get(i).getY() + ")") ;
		}
	}
	
	public static void getQuarterCircle() {
		int x = radius;
		int y = 0;
		double[] cW = new double[3];
		
		while(!(x == 0 && y == radius)) {
			
			cW[0] = Math.abs(radius-(Math.sqrt((x-1)*(x-1) + (y+1)*(y+1))));
			cW[1] = Math.abs(radius-(Math.sqrt((x)*(x) + (y+1)*(y+1))));
			cW[2] = Math.abs(radius-(Math.sqrt((x-1)*(x-1) + (y)*(y))));
				
			if(cW[0]<cW[1] && cW[0]<cW[2]) {
				lineTotals.add(1);
				lineType.add("Point");
				CoordsList.add(new Point(x-1,y+1));			
				x = x-1;
				y = y+1;
			}
			else if(cW[1]<cW[0] && cW[1]<cW[2]) {
				lineTotals.set(lineTotals.size()-1,lineTotals.get(lineTotals.size()-1) + 1);
				lineType.set(lineType.size()-1,"vertical line");
				CoordsList.add(new Point(x,y+1));
				y = y+1;
			}
			else if(cW[2]<cW[0] && cW[2]<cW[1]) {
				lineTotals.set(lineTotals.size()-1,lineTotals.get(lineTotals.size()-1) + 1);
				lineType.set(lineType.size()-1,"horizontal line");
				CoordsList.add(new Point(x-1,y));
				x = x-1;
			}
		}
	}
	
	public static void getFullCircle() {
		FullCoordsList.add(new Point(radius,0));
		//Top Right
		for(int i=0;i<CoordsList.size();i++) {
			if(CoordsList.get(i).getX() != 0 && CoordsList.get(i).getY() != 0) {
				FullCoordsList.add(new Point((int)CoordsList.get(i).getX(), (int)CoordsList.get(i).getY()));
			}
		}
		FullCoordsList.add(new Point(0,radius));
		//Top Left
		for(int i=CoordsList.size()-1;i>=0;i--) {
			if(CoordsList.get(i).getX() != 0 && CoordsList.get(i).getY() != 0) {
				FullCoordsList.add(new Point(0-(int)CoordsList.get(i).getX(), (int)CoordsList.get(i).getY()));
			}
		}
		FullCoordsList.add(new Point(-radius,0));
		//BottomLeft
		for(int i=0;i<CoordsList.size();i++) {
			if(CoordsList.get(i).getX() != 0 && CoordsList.get(i).getY() != 0) {
				FullCoordsList.add(new Point(0-(int)CoordsList.get(i).getX(), 0-(int)CoordsList.get(i).getY()));
			}
		}
		FullCoordsList.add(new Point(0,-radius));
		//BottomRight
		for(int i=CoordsList.size()-1;i>=0;i--) {
			if(CoordsList.get(i).getX() != 0 && CoordsList.get(i).getY() != 0) {
				FullCoordsList.add(new Point((int)CoordsList.get(i).getX(), 0-(int)CoordsList.get(i).getY()));
			}
		}
		
	}
}