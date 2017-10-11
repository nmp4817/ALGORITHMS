def getways(arr,m,n):
	print arr
	print n
	print m
	if n == 0:
		return 1
	if n < 0:
		return 0
	if m <= 0 and n >= 1:
		return 0
	return getways(arr,m-1,n) + getways(arr,m,n-arr[m-1])

if __name__ == '__main__':
	arr = [1,2,3]
	m = 3
	n = 4
	print getways(arr,m,n)