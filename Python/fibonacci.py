def fibonacci(n):
	if n == 1 or n == 0 :
		return 1
	ans = fibonacci(n-1) + fibonacci(n-2)
	return ans

# # Tail recursion fibonacci
# def fibonacci(n,a = 0,b = 1):
#     if n == 0:
#         return a
#     if n == 1:
#         return b
#     return fibonacci(n-1,b,a+b)


if __name__ == '__main__':
	n = raw_input("Enter the limit: ")
	# result = fibonacci(int(n))
	result = []
	for i in range(0,int(n)) :
		result.append(fibonacci(i))
	print 'First ',n,' element of fibonacci sequence are :',result