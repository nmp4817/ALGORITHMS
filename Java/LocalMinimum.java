import java.util.Arrays;

public class LocalMinimum {
	public static void main(String[] args) {
		int[][] arr = {{7,12,14,22},{8,4,6,6},{6,5,6,7},{5,2,10,6}};
		for( int i=0;i<4;i++ ) {
			for( int j=0;j<4;j++ ) {
				System.out.print(arr[i][j]+"\t");  
			}  
			System.out.println();  
		}  
		// System.out.println("Original Array:"+Arrays.deepToString(arr));

		Minimum local_minimum = find_local_minimum(arr,0,arr.length-1,0,arr[0].length-1);
		System.out.println("Local Minimum: ("+local_minimum.x+","+local_minimum.y+")");

	}

	public static Minimum find_local_minimum(int[][] arr,int ll,int hl,int lw,int hw) {
		// System.out.println(""+ll+hl+lw+hw);
		int n = (ll+hl)/2;
		int m = (lw+hw)/2;

		int[] middle_row = arr[n];
		int[] middle_column = new int[arr.length];
		for ( int i=0;i<arr.length;i++ ) {
			middle_column[i] = arr[i][m];
		}
		// System.out.println("Middle row:"+Arrays.toString(middle_row));
		// System.out.println("Middle column:"+Arrays.toString(middle_column));
		Minimum min = find_minimum(middle_row,middle_column,n,m);
		// System.out.println(""+min.x+min.y+arr[min.x][min.y]);
		int x = min.x;
		int y = min.y;

		// 8 boundary conditions
		if ( x == 0 && y == 0 ) {
			if ( arr[x][y] <= arr[x+1][y] && arr[x][y] <= arr[x][y+1]) return min;
			else return new Minimum(-1,-1);
		} else if ( x == hl && y == hw ) {
			if ( arr[x][y] <= arr[x-1][y] && arr[x][y] <= arr[x][y-1] )	return min;
			else return new Minimum(-1,-1);
		} else if ( x == hl && y == 0 ) {
			if ( arr[x][y] <= arr[x-1][y] && arr[x][y] <= arr[x][y+1] ) return min;
			else return new Minimum(-1,-1) ;
		} else if ( x == 0 && y == hw ) {
			if ( arr[x][y] <= arr[x+1][y] && arr[x][y] <= arr[x][y-1] )	return min;
			else return new Minimum(-1,-1);
		} else if ( x == 0 ) {
			if ( arr[x][y] <= arr[x+1][y] && arr[x][y] <= arr[x][y+1] && arr[x][y] <= arr[x][y-1] ) return min;
			else return new Minimum(-1,-1);
		} else if ( y == 0 ) {
			if ( arr[x][y] <= arr[x-1][y] && arr[x][y] <= arr[x+1][y] && arr[x][y] <= arr[x][y+1] )	return min;
			else return new Minimum(-1,-1);
		} else if ( x == hl ) {
			if ( arr[x][y] <= arr[x-1][y] && arr[x][y] <= arr[x][y+1] && arr[x][y] <= arr[x][y-1] )	return min;
			else return new Minimum(-1,-1);
		} else if ( y == hw ) {
			if ( arr[x][y] <= arr[x-1][y] && arr[x][y] <= arr[x+1][y] && arr[x][y] <= arr[x][y-1] ) return min;
			else return new Minimum(-1,-1);
		}
		
		if ( x>0 && arr[x][y] <= arr[x-1][y] ) {
			if ( x<hl && arr[x][y] <= arr[x+1][y] ) {
				if ( y>0 && arr[x][y] <= arr[x][y-1] ) {
					if ( y<hw && arr[x][y] <= arr[x][y+1] ) {
						return min;
					} else {
						if ( x>n ) return find_local_minimum(arr,n,hl,m,hw);
						else return find_local_minimum(arr,ll,n,m,hw);
					} 
				} else {
					if ( x>n ) return find_local_minimum(arr,n,hl,lw,m);
					else return find_local_minimum(arr,ll,n,lw,m);
				}
			} else  {
				if ( y>m ) return find_local_minimum(arr,n,hl,m,hw);
				else return find_local_minimum(arr,n,hl,lw,m);
			}
		} else {
			if ( y>m ) return find_local_minimum(arr,ll,n,m,hw);
			else return find_local_minimum(arr,ll,n,lw,m);
		}
	}

	public static Minimum find_minimum(int[] arr1,int[] arr2,int n,int m) {
		int l1 = arr1.length;
		int l2 = arr2.length;
		int l = l1+l2;
		int[] arr = new int[l];
		System.arraycopy(arr1, 0, arr, 0, l1);
   		System.arraycopy(arr2, 0, arr, l1, l2);
   		Minimum minimum_pos = new Minimum(n,arr[0]);
   		int minimum = arr[0];
   		// System.out.println("Combine Array:"+Arrays.toString(arr));

   		for ( int i=1;i<l;i++ ) {
   			if ( minimum > arr[i] ) {
   				minimum = arr[i];
   				if ( i<l1 ) minimum_pos = new Minimum(n,i);
   				else minimum_pos = new Minimum(i-l1,m);
   			}
   		}
   		
   		return minimum_pos;
	}
}

class Minimum {
	public final int x;
	public final int y;

	Minimum(int x,int y) {
		this.x = x;
		this.y = y;
	}
}