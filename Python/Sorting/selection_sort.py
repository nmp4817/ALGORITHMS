#Selection sort
def selection(arr):
	for i in range(0,len(arr)-1):
		smallest = arr[i]
		# k=i
		for j in range(i+1,len(arr)):
			if arr[j] < smallest:
				smallest = arr[j]
				arr[j] = arr[i]
				arr[i] = smallest
				# k = j
		# if k!=i:
		# 	arr[k] = arr[i]
		# 	arr[i] = smallest

	print 'Sorted: ',arr

if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,9,5,6]
	print 'Original: ',arr
	selection(arr)