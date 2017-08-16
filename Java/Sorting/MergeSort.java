import java.util.Arrays;

public class MergeSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,4};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = merge_sort(arr);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] merge_sort(int[] arr) {
		if ( arr.length == 1 ) {
			return arr;
		}
		System.out.println("left Array: "+Arrays.toString(arr));

		int[] left = Arrays.copyOfRange(arr,0,arr.length/2);
		int[] right = Arrays.copyOfRange(arr,arr.length/2,arr.length);
		// System.out.println("left Array: "+Arrays.toString(left));
		// System.out.println("right Array: "+Arrays.toString(right));

		int[] left_sorted = merge_sort(left);
		int[] right_sorted = merge_sort(right);
		
		return merge(left_sorted,right_sorted);
	}

	public static int[] merge(int[] arr1,int[] arr2) {

		int[] arr3 = new int[arr1.length+arr2.length];
		int i=0, j=0, k=0;
		while ( i<arr1.length && j<arr2.length ) {
			if ( arr1[i]<arr2[j] ) {
				arr3[k] = arr1[i];
				k++;
				i++;
			} else {
				arr3[k] = arr2[j];
				k++;
				j++;
			}
		}
		
		for(int m=i;m<arr1.length;m++) {
			arr3[k] = arr1[m];
			k++;
		}

		for(int n=j;n<arr2.length;n++) {
			arr3[k] = arr2[n];
			k++;
		}
		System.out.println("Inside Array: "+Arrays.toString(arr3));
		return arr3;
	}
}