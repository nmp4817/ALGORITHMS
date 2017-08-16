import java.util.Scanner;

public class KaratsubaMultiplication {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter an integer number1: ");
		int number1 = scanner.nextInt();
		System.out.println("Enter an integer number2: ");
		int number2 = scanner.nextInt();

		int result = karatsuba(number1,number2);
		System.out.println(""+result);
		
	}

	public static int karatsuba(int number1, int number2) {
		if ( number1<10 || number2<10 ) {
			return number1 * number2;
		}

		String n1 = Integer.toString(number1);
		int l1 = n1.length();
		// int num1[] = new int[n1.length()];
		String n2 = Integer.toString(number2);
		int l2 = n2.length();
		// int num2[] = new int[n2.length()];

		int m = Math.max(l1,l2);
		// int i=0,j=0;
		int m2 = m/2;
		// System.out.println(""+m2);

		int[] split_arr = new int[2];

		split_arr = split_int(number1,m2,l1,n1);
		int high1 = split_arr[0];
		int low1 = split_arr[1];
		// System.out.println(""+high1+" "+low1);

		split_arr = split_int(number2,m2,l2,n2);
		int high2 = split_arr[0];
		int low2 = split_arr[1];
		// System.out.println(""+high1+" "+low1);

		int z0 = karatsuba(low1,low2);
		int z1 = karatsuba((high1+low1),(high2+low2));
		int z2 = karatsuba(high1,high2);

		return (((z2)*(int)(Math.pow(10,2*m2)))+((z1-z2-z0)*(int)(Math.pow(10,m2)))+z0);
	}

	public static int[] split_int(int num, int split_ind,int l, String num_string) {
		int high=0,low=0;
		if ( l<=split_ind ) {
			low = num;
		} else {
			low = Integer.parseInt(num_string.substring(l-split_ind,l));
			high = Integer.parseInt(num_string.substring(0,l-split_ind));
		}

		int split_arr[] = {high,low};
		
		return split_arr;
	}
}