def fibonacci(n):
	if n == 1 or n == 0 :
		return 1
	ans = fibonacci(n-1) + fibonacci(n-2)
	return ans


if __name__ == '__main__':
	n = raw_input("Enter the limit: ")
	result = []
	for i in range(0,int(n)) :
		result.append(fibonacci(i))
	print 'First ',n,' element of fibonacci sequence are :',result