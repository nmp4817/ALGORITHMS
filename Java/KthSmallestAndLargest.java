import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import sorting.QuickSort;
     
public class KthSmallestAndLargest {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,8,10,17};
		System.out.println("Original Array: "+Arrays.toString(arr));
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Please enter integer between 0 and "+(arr.length-1)+": ");
		int k = scan.nextInt();
		int k_smallest = k_th_smallest(arr,k);
		int k_largest = k_th_smallest(arr,arr.length-k-1);

		System.out.println("Sorted Array: "+Arrays.toString(QuickSort.quick_sort(arr,0,arr.length-1)));
		System.out.println("k_th_smallest: "+k_smallest);
		System.out.println("k_th_largest: "+k_largest);
	}

	public static int k_th_smallest(int[] arr, int k) {
		int pivot = MedianOfMedians.median_of_medians(arr);
		ArrayList<Integer> lesser = new ArrayList<Integer>();
		ArrayList<Integer> greater = new ArrayList<Integer>();
		ArrayList<Integer> pivots = new ArrayList<Integer>();

		for ( int i=0;i<arr.length;i++ ) {
			if ( arr[i]<pivot ) lesser.add(arr[i]);
			else if ( arr[i]>pivot ) greater.add(arr[i]);			
			else pivots.add(arr[i]);
		}

		for (int j=0;j<pivots.size()-1;j++) lesser.add(pivots.get(j));

		int l_l = lesser.size();

		if ( k<l_l ) return k_th_smallest(convert_list_to_array(lesser),k);
		else if ( k>l_l ) return k_th_smallest(convert_list_to_array(greater),k-l_l-1);
		else return pivot;
	}

	public static int[] convert_list_to_array(ArrayList<Integer> arrlst) {
		int[] arr = new int[arrlst.size()];
		for ( int i=0;i<arr.length;i++ ) arr[i] = arrlst.get(i);
		return arr;
	}
}