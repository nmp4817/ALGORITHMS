import java.util.Arrays;

public class BubbleSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,4};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = bubble_sort(arr);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] bubble_sort(int[] arr) {
		int temp = 0;
		for ( int i=0;i<arr.length;i++ ) {
			for( int j=0;j<arr.length-i-1;j++ ) {
				if (arr[j]>arr[j+1]) {
					temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}

		return arr;
	}
}