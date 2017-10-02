import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
        
    # Function to find M-th to last element
	def mthToLast(self,M):
		ptr = self.head
		i = 1
		while ptr != None:
			if i == M:
				return ptr.data
			ptr = ptr.next
			i = i+1
		return 'NIL'
if __name__ == '__main__':
	try:
		values = []
		# values1 = []
		# values2 = []

		M = int(raw_input())
		L = str(raw_input())					# sys.stdin.read()

		values = L.split(" ")

		if len(values) < M:
			print 'NIL'
		else:
			print values[-M]

		# # if len(L) < 1000000:
		# # 	values = L.split(" ")
		# # 	# print values
		# # else:
		# # 	values1 = L[:len(L)/2].split(" ")
		# # 	values2 = L[(len(L)/2)+1:].split(" ")
		# # 	values = values1 + values2
		# # 	print values

		# # print values
		# llist = LinkedList()
		# # print values

		# for i in values:
		# 	# print i
		# 	llist.push(int(i))

		# print llist.mthToLast(M)

	except Exception as e:
		print str(e)

