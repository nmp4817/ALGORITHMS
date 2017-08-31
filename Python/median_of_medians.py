import time
start_time = time.time()
# import sys
# sys.path.insert(0, 'Sorting')
# from quick_sort import quick_sort

def median_of_medians(arr):

	# runs in --- seconds --- 0.00699996948242
	# better one (copied from net)

	# divide A into sublists of len 5
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
    if len(medians) <= 5:
        return sorted(medians)[len(medians)/2]
    else:
        return median_of_medians(medians)


#   # runs in ---seconds --- 0.00800013542175
#  	# mine one
	
# 	subarr = []
# 	l = len(arr)
# 	i=0

# 	# divide A into sublists of len 5
# 	while l > 0:
# 		if l < 5:
# 			end_index = i+l
# 		else:
# 			end_index = i+5
# 		temp = arr[i:end_index]
# 		subarr.append(quick_sort(temp,0,len(temp)-1))
# 		i = i+5
# 		l = l - 5
# 	# print subarr
	
# 	median_arr = find_median(subarr)
# 	# print median_arr

# 	l_m = len(median_arr)
# 	if l_m <= 5:
# 		return quick_sort(median_arr,0,l_m-1)[l_m/2]
# 	else:
# 		return median_of_medians(median_arr)
	

# def find_median(subarr):
# 	median = []
# 	for i in range(len(subarr)):
# 		median.append(subarr[i][len(subarr[i])/2])

# 	return median

if __name__ == '__main__':
	arr = [7,4,9,6,5,3,19,37,1,7,4,6,50,33,23,45,67,89,56,23,45,6,8,9,10,13,12,17,16,18,19,20,33,37]
	print 'Original: ',arr
	print 'Sorted: ',sorted(arr)
	# print 'Sorted: ',quick_sort(arr,0,len(arr)-1)
	median = median_of_medians(arr)
	print 'Median: ',median
	print "---seconds ---", (time.time()-start_time)

