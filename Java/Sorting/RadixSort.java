package soritng;
import java.util.Arrays;

public class RadixSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,40};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = radix_sort(arr);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] radix_sort(int[] arr) {
		int max_num = getMax(arr);
		// System.out.println(""+max_num);
		int num_of_digits = (Integer.toString(max_num)).length();
		// System.out.println(""+num_of_digits);

		for ( int i=0;i<num_of_digits;i++ ) {
			int[] index_count = new int[10];
			int[] result = new int[arr.length];

			for ( int j=0;j<10;j++ ) {
				index_count[j] = 0;
			}

			for ( int k=0;k<arr.length;k++ ) {
				result[k] = 0;
				index_count[(arr[k]/((int)(Math.pow(10,i))))%10] += 1;
			}
			// System.out.println(Arrays.toString(index_count));

			for ( int l=1;l<10;l++ ) {
				index_count[l] += index_count[l-1];
			}
			// System.out.println(Arrays.toString(index_count));

			for ( int m=arr.length-1;m>=0;m-- ) {
				result[index_count[(arr[m]/((int)(Math.pow(10,i))))%10] - 1] = arr[m];
				index_count[(arr[m]/((int)(Math.pow(10,i))))%10] -= 1;
			}

			arr = result;
		}
		return arr;
	}

	public static int getMax(int[] arr) {
		int max_num = arr[0];
		for ( int i=0;i<arr.length;i++ ) {
			if ( arr[i] > max_num ) {
				max_num = arr[i];
			}
		}

		return max_num;
	}
}