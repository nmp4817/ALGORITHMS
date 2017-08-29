def sec_largest(arr):

	# # 2n comparisions
	# maxi=arr[0]
	# maxi2=arr[1]
	# for i in range(1,len(arr)):
	# 	if maxi2<arr[i]:	
	# 		maxi2=arr[i]
	# 	if maxi<=arr[i]:
	# 		maxi2=maxi
	# 		maxi=arr[i]
	# return maxi2

	#n+logn-2 comparisions
	compared = find_max_tournament(0,len(arr)-1,arr)
	print compared
	compared2 = find_max_tournament(1,compared[0]-1,compared[1:])
	return compared2[1]

def find_max_tournament(i,j,arr):
	print i,j
	if i==j:
		compared=[]
		compared.append(1)
		compared.append(arr[i])
		return compared

	compared1 = find_max_tournament(i,(i+((j-i)/2)),arr)
	print "compared1",compared1
	compared2 = find_max_tournament(1+(i+((j-i)/2)),j,arr)
	print "compared2",compared2
	# print "before",compared1
	if compared1[1] > compared2[1]:
		k = compared1[0]+1
		# compared1[0] = k
		compared1[0] += 1
		# compared1[k] = compared2[1]
		compared1.append(compared2[1])
		# print "after",compared1
		return compared1

	else:
		k = compared2[0]+1
		# compared2[0] = k
		compared2[0] += 1
		# compared2[k] = compared1[1]
		compared2.append(compared1[1])
		return compared2

if __name__ == '__main__':
	arr = [1,2,3,4,5,6]
	result2 = sec_largest(arr)
	print result2