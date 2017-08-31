from median_of_medians import median_of_medians

def k_th_smallest(arr,k):
	pivot = median_of_medians(arr)
	# print pivot

	# better one (copied from net)
	
	# partitioning step
	low = [j for j in arr if j < pivot]
	high = [j for j in arr if j > pivot]

	# for duplicate entries
	pivots = [j for j in arr if j == pivot]
	
	for i in range(len(pivots)-1):
		low.append(pivot)

	i = len(low)
	if k < i:
	    return k_th_smallest(low,k)
	elif k > i and i!=0:
	    return k_th_smallest(high,k-i-1)
	else: #pivot = k
	    return pivot


	# mine one

	# lesser = []
	# greater = []
	# pivots = []
	
	# for i in range(0,len(arr)):
	# 	if arr[i] < pivot:
	# 		lesser.append(arr[i])
	# 	elif arr[i] > pivot:
	# 		greater.append(arr[i])
	# 	else:
	# 		pivots.append(arr[i])

	# for i in range(len(pivots)-1):
	# 	lesser.append(pivot)

	# # print lesser
	# # print greater

	# l_l = len(lesser)	
	# # print l_l
	
	# if k < l_l:
	# 	return k_th_smallest(lesser,k)
	# elif k > l_l and l_l != 0:
	# 	return k_th_smallest(greater,k-l_l-1)
	# else:
	# 	return pivot

if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,7,4,6,50,33,23,45,67,89,56,23,45,6,8,9,10,13,12,17,16,18,19,20,33,37]
	print 'Original: ',arr
	print 'Sorted: ',sorted(arr)
	# print 'Sorted: ',quick_sort(arr,0,len(arr)-1)

	k = int(raw_input("Please enter integer between 0 and "+str(len(arr)-1)+": "))
	k_smallest = k_th_smallest(arr,k)
	k_largest = k_th_smallest(arr,len(arr)-k-1)
	print 'KTH_SMALLEST: ',k_smallest
	print 'KTH_LARGEST: ',k_largest
	