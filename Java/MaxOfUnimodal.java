import java.util.Arrays;

public class MaxOfUnimodal {
	public static void main(String[] args) {
		int[] arr = {1,3,4,5,7,8,8,10,10,12,13,14,14,16,15,14,10,9,6,2};
		System.out.println("Original Array: "+Arrays.toString(arr));
		int max = max_of_unimodal(arr);
		System.out.println("Max Of Unimodal: "+max);

		int[] arr1 = {-10,-1,0,3,10,11,30,50,100};
		System.out.println("Original Array: "+Arrays.toString(arr1));
		System.out.println("A[i] == i: "+find_i_equal_ai(arr1,0,arr1.length-1));
	}

	public static int max_of_unimodal(int[] arr) {
		// System.out.println("Array: "+Arrays.toString(arr));
		if ( arr.length == 1 ) return arr[0];

		if ( arr[(arr.length/2)-1] > arr[arr.length/2] ) return max_of_unimodal(Arrays.copyOfRange(arr,0,arr.length/2));
		else return max_of_unimodal(Arrays.copyOfRange(arr,arr.length/2,arr.length));
	}

	public static int find_i_equal_ai(int[] arr,int low,int high) {
		if ( high >= low ) {
			int mid = (low+high)/2;

			if ( arr[mid] == mid ) return mid;
			else if ( arr[mid] > mid ) return find_i_equal_ai(arr,low,mid-1);
			else return find_i_equal_ai(arr,mid+1,high);
		}

		return -1;
	}
}