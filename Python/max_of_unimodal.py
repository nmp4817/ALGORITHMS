def find_max(arr):
	print arr
	if len(arr)==1:
		return arr[0]
	
	if arr[(len(arr)/2)-1] > arr[len(arr)/2]:
		return find_max(arr[:len(arr)/2])
	else:
		return find_max(arr[len(arr)/2:])

def find_i_equal_ai(arr,low,high):
	if high >= low:		
		mid = (low+high)/2

		if arr[mid] == mid:
			return mid
		elif arr[mid] > mid:
			return find_i_equal_ai(arr,low,mid-1)
		elif arr[mid] < mid:
			return find_i_equal_ai(arr,mid+1,high)

	return -1

if __name__ == '__main__':
	arr = [1,3,4,5,7,8,8,10,10,12,13,14,14,16,15,14,10,9,6,2]
	print 'Original: ',arr
	print 'Maximum: ',find_max(arr)

	arr = [-10,-1,0,3,10,11,30,50,100]
	print 'Original: ',arr
	print 'A[i] == i: ',find_i_equal_ai(arr,0,len(arr)-1)
