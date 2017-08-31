package soritng;
import java.util.Arrays;

public class InsertionSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,4};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = insertion_sort(arr);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] insertion_sort(int[] arr) {
		int key = 0,j=0;
		for ( int i=1;i<arr.length;i++ ) {
			key = arr[i];
			j = i-1;
			while ( j>=0 && arr[j]>key ) {
				arr[j+1] = arr[j];
				j = j-1;
			}
			arr[j+1] = key;
		}

		return arr;
	}
}