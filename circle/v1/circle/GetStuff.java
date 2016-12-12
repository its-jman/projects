package circle;

import java.awt.Point;
import java.util.ArrayList;
import java.util.Scanner;

public class GetStuff
{	
	public static int[] coordTotal = new int[1600];
	public static String[] lineType = new String[1600];
	private static double[] way = new double[3];
	private static double[] cW = new double[3];
	public static int[] fX = new int[1600];
	public static int[] fY = new int[1600];
	public static ArrayList<Point> coordList = new ArrayList<Point>();
	public static int width = 0;
	private static Scanner s = new Scanner(System.in);
	public static int[] horLineTotal = new int[1600];
	public static int[] vertLineTotal = new int[1600];
	
	public static void main(String[] args) {
		
		getWidth();
		getCoords();
		
		for(int i=0;i<1600;i++) {
			coordTotal[i] = fX[i] + fY[i];
		}
		
		changeZeros();
		findLineType();
		findLineTotals();
		printStuff();
	}
	
	public static void printStuff() {
		for(int i=0;i<1600;i++) {
			if(fX[i] < 10 && fY[i] <10){
				System.out.println("(" + fX[i] + ", " + fY[i] + ")");
			}
		}
		for(int j=width;j>=0;j--) {
			if(vertLineTotal[j] > 0) {
				System.out.print("\n" + vertLineTotal[j] + " blocks vertical\n");
				
			}
			
		}
		for(int i=0;i<1600;i++) {
			if(lineType[i].equalsIgnoreCase("singPoint")) {
				System.out.print("\nPoint\n");
			}
		}
		
		for(int j=0;j<=width;j++) {
			if(horLineTotal[j] > 0) {
				System.out.print("\n" + horLineTotal[j] + " blocks horizontal\n");
			}
		}
		for(int i=0;i<coordList.size();i++) {
			System.out.print("\ncoordList[" + i + "]: " + coordList.get(i).getX() + ", " + coordList.get(i).getY());
		}
		
	}
	
	public static void findLineTotals() {
		for(int i=0;i<1600;i++) {
			for(int j=0;j<=width;j++) {
				if(lineType[i].equalsIgnoreCase("vertLine")) {
					if(fX[i] == j) {
						vertLineTotal[fX[i]]++;
					}
				}
				else if(lineType[i].equalsIgnoreCase("horLine")) {
					if(fY[i] == j) {
						horLineTotal[fY[i]]++;
					}
				}
				else if(lineType[i].equalsIgnoreCase("singPoint")) {
					if(fY[i] == j) {
						//horLineTotal[fY[i]]++;
					}
				}
			}
		}
	}
	
	public static void findLineType() {
		for(int i=0;i<1600;i++) {
			if(coordTotal[i] != 0) {
				if(fX[i] == fX[i+1] || fX[i] == fX[i-1]) {
					lineType[i] = "vertLine";
					
				}
				else if(fY[i] == fY[i+1] || fY[i] == fY[i-1]) {
					lineType[i] = "horLine";
				}
				else {
					lineType[i] = "singPoint";
				}
			}
			else {
				lineType[i] = "noPoint";
			}
		}
	}
	
	public static void changeZeros() {
		for(int i=0;i<1600;i++) {
			if(coordTotal[i] == 0) {
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
			way[0] = Math.sqrt((x-1)*(x-1) + (y+1)*(y+1));
			way[1] = Math.sqrt((x)*(x) + (y+1)*(y+1));
			way[2] = Math.sqrt((x-1)*(x-1) + (y)*(y));
			
			cW[0] = Math.abs(width-way[0]);
			cW[1] = Math.abs(width-way[1]);
			cW[2] = Math.abs(width-way[2]);
			
			if(cW[0]<cW[1] && cW[0]<cW[2]) {
				fX[i] = (int) (x-1);
				fY[i] = (int) (y+1);
				x = x-1;
				y = y+1;
			}
			else if(cW[1]<cW[0] && cW[1]<cW[2]) {
				fX[i] = (int) (x);
				fY[i] = (int) (y+1);
				y = y+1;
			}
			else if(cW[2]<cW[0] && cW[2]<cW[1]) {
				fX[i] = (int) (x-1);
				fY[i] = (int) (y);
				x = x-1;
			}
			i++;
		}
	}

	public static void getWidth() {
		while(width == 0) {
			try 
			{
				System.out.print("Enter the width(Radius 1): ");
				width = Integer.parseInt(s.nextLine());
			}
			catch(NumberFormatException e)
			{
				System.out.print("\n" +"Please enter an integer greater than 0.\n");
			}
		}
	}
}