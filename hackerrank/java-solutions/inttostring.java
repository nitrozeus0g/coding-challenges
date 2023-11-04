import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String x = Integer.toString(n);
		if (n < -100 || n > 100) {
			System.out.println("Wrong answer");
		} else if(x.length() != 0) {
			System.out.println("Good job");
		} else {
			System.out.println("Wrong answer");
		}
	}
}

