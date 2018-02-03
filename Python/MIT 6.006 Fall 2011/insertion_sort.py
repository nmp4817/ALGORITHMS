# #taking input array from user
# num_array = list()
# num = raw_input("Enter how many elements you want:")
# print 'Enter numbers in array: '
# for i in range(int(num)):
#     n = raw_input("num :")
#     num_array.append(int(n))
# print 'ARRAY: ',num_array

# #reading input array from file
# with open('data.txt', 'r') as myfile:
#     data=myfile.read().replace('\n', '')
#     num_array = data.split(",")


#Insertion sort : compare ith element to elements from 0 to i-1 (i.e put arr[i] into Sorted array arr[0:i-1])
#O(1) extra space

def insertion(arr):                                                       #O(n^2)
	for i in range(1,len(arr)):                                           #O(n) elements
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:                                        #O(n) swaps
			# arr[j+1],arr[j] = arr[j],key                                #swapping immidiately
			arr[j+1] = arr[j]			
			j = j-1
		arr[j+1] = key
	print 'Sorted: ',arr

def main():
	arr = [7,4,9,6,5,3,19,37,1,6,9,5]
	print 'Original: ',arr
	insertion(arr)

if __name__ == '__main__':
	import profile
	profile.run("main()")	