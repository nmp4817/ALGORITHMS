def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(0,len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print 'Sorted: ', arr


if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,6,9,13]
	print 'Original: ',arr
	bubble_sort(arr)
