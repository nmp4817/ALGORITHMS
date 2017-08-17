import math

def karatsuba(num1,num2):
	if (num1<10) or (num2<10):
		return num1*num2
	n1 = str(num1)
	l1 = len(n1)
	n2= str(num2)
	l2 = len(n2)
	m = max(l1,l2)
	# print m
	# m2=int(math.ceil(float(m)/2))
	m2 = m/2
	# print m2
	
	split_arr = split_int(num1,m2,l1,n1)
	high1 = int(split_arr[0])
	low1 = int(split_arr[1])
	# print high1
	# print low1

	split_arr = split_int(num2,m2,l2,n2)
	high2 = int(split_arr[0])
	low2 = int(split_arr[1])
	# print high2
	# print low2
	
	z0 = karatsuba(low1,low2)
	z1 = karatsuba((high1+low1),(high2+low2))
	z2 = karatsuba(high1,high2)
	
	# print z0
	# print z1
	# print z2
	return (((z2)*(math.pow(10,2*m2)))+((z1-z2-z0)*(math.pow(10,m2)))+z0)

def split_int(num,split_ind,l,num_string):
	if l <= split_ind:
		low = num
		high = 0
	else:
		low = int(num_string[l-split_ind:])
		high = int(num_string[:l-split_ind])

	return [high,low]

if __name__ == '__main__':
	num1 = raw_input("Enter number 1: ")
	num2 = raw_input("Enter number 2: ")
	result = karatsuba(num1,num2)
	print result
