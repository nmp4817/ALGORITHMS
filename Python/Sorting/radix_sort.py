import math

def radix_sort(arr):
	# print len(arr)
	max_num = max(arr)
	# print max_num
	num_of_digits = len(str(max_num))
	# print num_of_digits
	
	for i in range(0,num_of_digits):
		index_count = []
		result = []

		for j in range(0,10):
			index_count.append(0)

		for l in range(0,len(arr)):
			result.append(0)
			index_count[(arr[l]/(int(math.pow(10,i))))%10] += 1
		# print index_count

		for k in range(1,10):
			index_count[k] += index_count[k-1]
		# print index_count

		for m in range(len(arr)-1,-1,-1):
			result[index_count[(arr[m]/(int(math.pow(10,i))))%10] - 1] = arr[m]
			index_count[(arr[m]/(int(math.pow(10,i))))%10] -= 1
		
		arr = result

	return result

if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,7,4,6,5]
	print 'Original: ',arr
	sorted_arr = radix_sort(arr)
	print 'Sorted: ',sorted_arr