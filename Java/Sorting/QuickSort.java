import java.util.Arrays;

public class QuickSort {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3,19,37,1,7,4,6,40};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int[] sorted_arr = quick_sort(arr,0,arr.length-1);
		System.out.println("Sorted Array: "+Arrays.toString(sorted_arr));
	}

	public static int[] quick_sort(int[] arr,int left,int right) {
		if ( left<right ) {
			// int pivot_index = hoare_partition(arr,left,right);
			// quick_sort(arr,left,pivot_index);
			// quick_sort(arr,pivot_index+1,right);
			int pivot_index = lomuto_partition(arr,left,right);
			quick_sort(arr,left,pivot_index-1);
			quick_sort(arr,pivot_index+1,right);
		}
		return arr;
	}

	public static int hoare_partition(int[] arr,int left,int right) {
		int pivot = arr[left];
		int lo = left-1;
		int hi = right+1;
		// int pivot = arr[right]
		// int lo = left
		// int hi = right-1

		while ( true ) {
			lo = lo+1;
			hi = hi-1;
			while ( arr[lo]<pivot ) {
				lo = lo+1;
			}	
			while ( arr[hi]>pivot ) {
				hi = hi-1;
			}
			if ( lo>=hi ) {
				return hi;
			}
			
			int temp = arr[lo];
			arr[lo] = arr[hi];
			arr[hi] = temp;
			// lo = lo+1
			// hi = hi-1
		}
	}

	public static int lomuto_partition(int[] arr,int lo,int hi) {
		int pivot = arr[hi];
		int i = lo-1;
		
		for ( int j=lo;j<hi;j++) {
			if ( arr[j] < pivot ) {
				i = i+1;
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
		
		int temp=arr[i+1];
		arr[i+1]=arr[hi];
		arr[hi]=temp;

		return i+1;
	}
}