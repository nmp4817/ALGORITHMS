import java.util.Arrays;
import sorting.QuickSort;

public class MedianOfMedians {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,8,10,17};
		System.out.println("Original Array: "+Arrays.toString(arr));
		
		int median = median_of_medians(arr);

		System.out.println("Sorted Array: "+Arrays.toString(QuickSort.quick_sort(arr,0,arr.length-1)));
		System.out.println("Median: "+median);
	}

	public static int median_of_medians(int[] arr) {
		int num_of_arr = (int)Math.ceil((double)arr.length/5);
		int[][] subarr = new int[num_of_arr][];

		int last_size = ( arr.length%5 == 0 ) ? 5 : arr.length%5;
		int size_of_arr = 5;

		for ( int i=0;i<num_of_arr;i++ ) {
			if ( i == num_of_arr-1 ) size_of_arr = last_size;
			// System.out.println(""+size_of_arr);
			subarr[i] = new int[size_of_arr];
			System.arraycopy(arr,i*5,subarr[i],0,size_of_arr);
			subarr[i] = QuickSort.quick_sort(subarr[i],0,size_of_arr-1);
		}

		// System.out.println("Original Array: "+Arrays.deepToString(subarr));

		int[] median_arr = find_median(subarr);
		// System.out.println("Median Array: "+Arrays.toString(median_arr));
		
		int l_m = median_arr.length;
		
		
		if ( l_m <= 5 ) return QuickSort.quick_sort(median_arr,0,l_m-1)[l_m/2];
		else return median_of_medians(median_arr);
	}

	public static int[] find_median(int[][] subarr) {
		int l = subarr.length;
		int[] median = new int[l];
		for ( int i=0;i<l;i++ ) {
			median[i] = subarr[i][subarr[i].length/2];
		}

		return median;
	} 
}