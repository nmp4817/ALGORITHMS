import java.util.Arrays;

public class SelectionSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,4};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = selection_sort(arr);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] selection_sort(int[] arr) {
		int smallest = 0,k=0;
		for ( int i=0;i<arr.length-1;i++ ) {
			smallest = arr[i];
			// k=i;
			// System.out.println(arr[i]+"before:"+Arrays.toString(arr));
			for ( int j = i+1;j<arr.length;j++ ) {
				if ( arr[j]<smallest ) {
					smallest = arr[j];
					arr[j] = arr[i];
					arr[i] = smallest;
					// k = j;
				}
			}
			// if (k!=i) {
			// 	arr[k] = arr[i];
			// 	arr[i] = smallest;	
			// }
			// System.out.println(k+"after:"+Arrays.toString(arr));
		}

		return arr;
	}
}