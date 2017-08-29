import java.util.Arrays;
import java.util.ArrayList;

public class SecondLargest {
	public static void main(String[] args) {
		int[] arr = {7,4,9,6,5,3};
		System.out.println("Original Array: "+Arrays.toString(arr));

		int result = sec_largest(arr); 
		System.out.println("Second Largest: "+result);
	}

	public static int sec_largest(int[] arr) {
		
		// // 2n comparisions
		// int maxi = arr[0],maxi2 = arr[1];
		// for ( int i=1;i<arr.length;i++ ) {
		// 	if ( maxi2<arr[i] ) {
		// 		maxi2 = arr[i];
		// 	}
		// 	if ( maxi<=arr[i] ) {
		// 		maxi2 = maxi;
		// 		maxi = arr[i];
		// 	}
		// }
		// return maxi2;


		// n+log2-n comparisions
		ArrayList<Integer> compared = find_max_tournament(0,arr.length-1,arr);
		int[] com = new int[compared.size()];
		for (int i = 0; i < com.length; i++) {
    		com[i] = compared.get(i);
		}
		// System.out.println("Original Array: "+Arrays.toString(com));
		ArrayList<Integer> compared2 = find_max_tournament(1,com[0]-1,Arrays.copyOfRange(com,1,com.length));
		return compared2.get(1);
	}

	public static ArrayList<Integer> find_max_tournament(int i,int j,int[] arr) {
		// System.out.println(""+i+","+j);
		if ( i==j ) {
			ArrayList<Integer> compared = new ArrayList<Integer>();
			compared.add(1);
			compared.add(arr[i]);
			return compared;
		}

		ArrayList<Integer> compared1 = find_max_tournament(i,i+((j-i)/2),arr);
		ArrayList<Integer> compared2 = find_max_tournament(1+i+((j-i)/2),j,arr);

		if ( compared1.get(1) > compared2.get(1) ) {
			int k = compared1.get(0)+1;
			compared1.set(0,k);
			compared1.add(compared2.get(1));
			return compared1;
		} else {
			int k = compared2.get(0)+1;
			compared2.set(0,k);
			compared2.add(compared1.get(1));
			return compared2;
		}
	}
}