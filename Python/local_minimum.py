import numpy as np
def find_local_minimum(arr,ll,hl,lw,hw):
	
	n = (ll+hl)/2
	m = (lw+hw)/2

	(x,y) = find_min(arr[n,0:hw+1],arr[0:hl+1,m],n,m)
	# print arr[x,y] 
	
	# print ll,hl,lw,hw
	
	# print x,y

	#8 boundary conditions
	if x == 0 and y == 0:
		if arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x][y+1]:
			return (x,y)
		else:
			return -1

	elif x == hl and y == hw:
		if arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x][y-1]:
			return (x,y)
		else:
			return -1

	elif x == hl and y == 0:
		if arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x][y+1]:
			return (x,y)
		else:
			return -1 

	elif x == 0 and y == hw:
		if arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x][y-1]:
			return (x,y)
		else:
			return -1

	elif x == 0:
		if arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x][y+1] and arr[x][y] <= arr[x][y-1]:
			return (x,y)
		else:
			return -1

	elif y == 0:
		if arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x][y+1]:
			return (x,y)
		else:
			return -1

	elif x == hl:
		if arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x][y+1] and arr[x][y] <= arr[x][y-1]:
			return (x,y)
		else:
			return -1

	elif y == hw:
		if arr[x][y] <= arr[x-1][y] and arr[x][y] <= arr[x+1][y] and arr[x][y] <= arr[x][y-1]:
			return (x,y)
		else:
			return -1
	
	if x>0 and arr[x][y] <= arr[x-1][y]:
		if x<hl and arr[x][y] <= arr[x+1][y]:
			if y>0 and arr[x][y] <= arr[x][y-1] :
				if y<hw and arr[x][y] <= arr[x][y+1]:
					return (x,y)
				else:
					if x>n:
						return find_local_minimum(arr,n,hl,m,hw)
					else:
						return find_local_minimum(arr,ll,n,m,hw)
			else:
				if x>n:
						return find_local_minimum(arr,n,hl,lw,m)
				else:
					return find_local_minimum(arr,ll,n,lw,m)
		else:
			if y>m:
				return find_local_minimum(arr,n,hl,m,hw)
			else:
				return find_local_minimum(arr,n,hl,lw,m)
	else:
		if y>m:
			return find_local_minimum(arr,ll,n,m,hw)
		else:
			return find_local_minimum(arr,ll,n,lw,m)

def find_min(arr1,arr2,n,m) :
	minimum = arr1[0]
	l1=len(arr1)
	l2=len(arr2)
	arr = np.concatenate([arr1,arr2])
	l=len(arr)

	# arr1.extend(arr2)
	for i in range(l):
		if minimum > arr[i]:
			minimum = arr[i]
			if i < l1:
				minimum_pos = (n,i)
			else:
				minimum_pos = (i-l1,m)
	return minimum_pos

if __name__ == '__main__':
	arr = [[7,12,14,22],[8,4,2,6],[6,5,6,7],[5,6,10,6]]
	print 'Original: \n',np.matrix(arr)
	arr = np.array(arr)
	# print np.shape(arr)[0]
	# print np.shape(arr)[1]
	local_minimum = find_local_minimum(arr,0,np.shape(arr)[0]-1,0,np.shape(arr)[1]-1)
	print 'Local Minimum: ',local_minimum