def count_inversion(arr):
	if len(arr) == 1:
		return (arr,0)
	left = arr[:len(arr)/2]
	right = arr[(len(arr)/2):]
	# print left
	# print right
	left_sorted,num_of_left_inversions = count_inversion(left)
	right_sorted,num_of_right_inversions = count_inversion(right)
	
	return count_splitInversions(left_sorted,right_sorted,num_of_left_inversions+num_of_right_inversions)

def count_splitInversions(arr1,arr2,total_num_of_inversions):
	arr3 = []
	j = 0
	i = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i]<arr2[j]:
			arr3.append(arr1[i])
			i = i+1
		else:
			arr3.append(arr2[j])
			# for l in range(i,len(arr1)):
			# 	print "(",arr1[l],",",arr2[j],")"
			j = j+1
			total_num_of_inversions += len(arr1) - i

	for k in range(i,len(arr1)):
		arr3.append(arr1[k])

	for m in range(j,len(arr2)):
		arr3.append(arr2[m])

	# print 'Inside: ',arr3

	return (arr3,total_num_of_inversions)



if __name__ == '__main__':
	arr = [7,4,9,6,5,3]
	print 'Original: ',arr
	sorted_arr,num_of_inversions = count_inversion(arr)
	print 'Number Of Inversions: ',num_of_inversions