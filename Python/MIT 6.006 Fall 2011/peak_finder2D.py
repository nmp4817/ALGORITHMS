#Peak finding for two dimension.
import numpy as np

arr = []
n = 0
m = 0

#Greedy Ascent Algorithm
def peak_finder1(i,j):                      #Time Complexity: T(n) = T(n/4) + O(1) = O(n^2)
	if i > 0 and arr[i - 1][j] > arr[i][j]:
		return peak_finder1(i - 1, j)
	elif i < n - 1 and arr[i + 1][j] > arr[i][j]:
		return peak_finder1(i + 1, j)
	elif j > 0 and arr[i][j - 1] > arr[i][j]:
		return peak_finder1(i, j - 1);
	elif j < m - 1 and arr[i][j + 1] > arr[i][j]:
		return peak_finder1(i, j + 1);
	else:
		return arr[i][j];

def peak_finder2(nArr):                      #Time Complexity: T(n) = T(n/2) + O(1) = O(logn) 
	# print nArr
	
	j = len(nArr[0])/2
	i = find_global_max(nArr[:,j])

	if i > 0 and nArr[i - 1][j] > nArr[i][j]:   #up side element bigger
		return peak_finder2(nArr[0:i,:])
	elif i < len(nArr) - 1 and nArr[i + 1][j] > nArr[i][j]:  #below side element bigger
		return peak_finder2(nArr[i+1:len(nArr),:])
	elif j > 0 and nArr[i][j - 1] > nArr[i][j]:     #left side element bigger
		return peak_finder2(nArr[:,0:j]);
	elif j < len(nArr[0]) - 1 and nArr[i][j + 1] > nArr[i][j]:   #right side element bigger
		return peak_finder2(nArr[:,j+1:len(nArr[0])]);
	else:
		return nArr[i][j];

def find_global_max(col):
	# print col
	m = max(col)
	# print np.where(col==m)
	return np.where(col==m)[0][0]

if __name__ == "__main__":
	arr  = [[3,7,56,78],[44,5,4,93],[3,3,56,6],[67,78,8,8]]
	n = len(arr)
	m = len(arr[0])
	print(peak_finder1(0,0))
	print(peak_finder2(np.array(arr)))