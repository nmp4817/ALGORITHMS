#Peak finding for one dimension.

def peak_finder1(arr):                      #Time Complexity: O(n)
		if arr[1] <= arr[0]:
			return arr[0]
		elif arr[len(arr)-2] <= arr[len(arr)-1]:
			return arr[len(arr)-1]
		else:					
			for i in range(1,len(arr)-1):
				if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
					return arr[i]

def peak_finder2(arr):                      #Time Complexity: T(n) = T(n/2) + O(1) = O(logn) 
	n = len(arr)
	# print arr
	if n == 1:
		return arr[0]
	elif n == 2:
		if arr[0] >= arr[1]:
			return arr[0]
		else:
			return arr[1]
	else:
		if arr[n/2] < arr[(n/2)-1]:
			return peak_finder2(arr[0:(n/2)])
		elif arr[n/2] < arr[n/2+1]:
			return peak_finder2(arr[(n/2)+1:n])
		else:
			return arr[n/2]
	return -1



if __name__ == "__main__":
	arr  = [3,7,56,98,44,5,4,3,3,3,5,6,67,78,8,8,9,5,4,3,3,4,4,4,5,3,3434,34,34,34,3,43434,3,4,34,4,34,3,43,4,35,54,56,6,76,87,8,89,46,5]
	# print(peak_finder1(arr))
	print(peak_finder2(arr))