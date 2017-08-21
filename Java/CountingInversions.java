import java.util.Arrays;

public class CountingInversions {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3};
		System.out.println("Original Array: "+Arrays.toString(arr));

		ReturningValues result = count_inversion(arr); 
		int num_of_inversions = result.num_of_inversions;
		System.out.println("Number Of Inversions: "+num_of_inversions);
	}

	public static ReturningValues count_inversion(int[] arr) {
		if ( arr.length == 1 ) {
			return new ReturningValues(arr,0);
		}
		// System.out.println("left Array: "+Arrays.toString(arr));

		int[] left = Arrays.copyOfRange(arr,0,arr.length/2);
		int[] right = Arrays.copyOfRange(arr,arr.length/2,arr.length);

		// System.out.println("left Array: "+Arrays.toString(left));
		// System.out.println("right Array: "+Arrays.toString(right));

		ReturningValues left_inversions = count_inversion(left);
		ReturningValues right_inversions = count_inversion(right);
		
		return count_splitInversions(left_inversions,right_inversions);
	}

	public static ReturningValues count_splitInversions(ReturningValues left_inversions,ReturningValues right_inversions) {
		int[] arr1 = left_inversions.sorted_arr;
		int[] arr2 = right_inversions.sorted_arr;
		int num_of_left_inversions = left_inversions.num_of_inversions;
		int num_of_right_inversions = right_inversions.num_of_inversions;
		int total_inversions = num_of_left_inversions + num_of_right_inversions;
		int[] arr3 = new int[arr1.length+arr2.length];
		int i=0, j=0, k=0;	

		while ( i<arr1.length && j<arr2.length ) {
			if ( arr1[i]<arr2[j] ) {
				arr3[k] = arr1[i];
				k++;
				i++;
			} else {
				arr3[k] = arr2[j];
				// for(int l=i;l<arr1.length;l++) {
				// 	System.out.println("("+arr1[l]+","+arr2[j]+")");
				// }
				k++;
				j++;
				total_inversions += arr1.length-i;
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
		// System.out.println("Inside Array: "+Arrays.toString(arr3));
		return new ReturningValues(arr3,total_inversions);

	}
}

class ReturningValues {
    public final int num_of_inversions;
    public final int[] sorted_arr;

    public ReturningValues(int[] sorted_arr, int num_of_inversions) {
        this.sorted_arr = sorted_arr;
        this.num_of_inversions = num_of_inversions;
    }
}