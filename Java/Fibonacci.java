import java.util.Scanner;
import java.util.Arrays;

public class Fibonacci {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the limit: ");
		int n = scan.nextInt();
		int[] result = new int[n];
		for ( int i=0;i<n;i++ ) {
			result[i] = fibonacci(i);
		}
		System.out.println("First "+n+" element of fibonacci sequence are :"+Arrays.toString(result));
	}

	public static int fibonacci(int n) {
		if ( n==1 || n==0 ) {
			return 1;
		}
		int ans = fibonacci(n-1) + fibonacci(n-2);
		return ans;
	}
}