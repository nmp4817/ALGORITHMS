def quick_sort(arr,left,right):
	if left<right:
		# pivot_index = hoare_partition(arr,left,right)
		# quick_sort(arr,left,pivot_index)
		# quick_sort(arr,pivot_index+1,right)
		pivot_index = lomuto_partition(arr,left,right)
		quick_sort(arr,left,pivot_index-1)
		quick_sort(arr,pivot_index+1,right)
	return arr

def hoare_partition(arr,left,right):
	pivot = arr[left]
	lo = left-1
	hi = right+1
	# pivot = arr[right]
	# lo = left
	# hi = right-1

	while True:
		lo = lo+1
		hi = hi-1
		while arr[lo]<pivot:
			lo = lo+1
		while arr[hi]>pivot:
			hi = hi-1
		if lo>=hi:
			return hi
		
		temp = arr[lo]
		arr[lo] = arr[hi]
		arr[hi] = temp
		# lo = lo+1
		# hi = hi-1

		# print arr

def lomuto_partition(arr,lo,hi):
	pivot = arr[hi]
	i = lo-1
	
	for j in range(lo,hi):
		if arr[j] < pivot:
			i = i+1
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
	
	temp=arr[i+1]
	arr[i+1]=arr[hi]
	arr[hi]=temp

	return i+1
		
if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,7,4,6,50]
	print 'Original: ',arr
	sorted_arr = quick_sort(arr,0,len(arr)-1)
	print 'Sorted: ',sorted_arr