#divide array in half recrusively and merge them to make them sorted
#O(n) extra space
#There is in-place merge-sort which use O(1) extra space and O(nlogn) but constants are large, so running time is not good. 

def merge_sort(arr):                            #T(n) = C1 + 2T(n/2) + O(n) = O(nlogn)
	if len(arr) == 1:
		return arr
	left = arr[:len(arr)/2]                     #C1 = divide complexity constant 
	right = arr[(len(arr)/2):]
	# print left
	# print right
	left_sorted = merge_sort(left)              #recursion T(n/2)
	right_sorted = merge_sort(right)            #recursion T(n/2)
	
	return merge(left_sorted,right_sorted)      #merging O(n)

def merge(arr1,arr2):
	arr3 = []
	j = 0
	i = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i]<arr2[j]:
			arr3.append(arr1[i])
			i = i+1
		else:
			arr3.append(arr2[j])
			j = j+1

	for k in range(i,len(arr1)):
		arr3.append(arr1[k])

	for m in range(j,len(arr2)):
		arr3.append(arr2[m])

	print 'Inside: ',arr3

	return arr3


if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,7,4,6,5]
	print 'Original: ',arr
	sorted_arr = merge_sort(arr)
	print 'Sorted: ',sorted_arr