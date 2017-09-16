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

	#Function to find Location by number of node
	def find_loc_by_number(self,number_of_node):
		# List is empty
		if self.head == None:
			return (None,None)

		if number_of_node == 1:
			print "here"
			return (self.head,None)

		ptr = self.head.next
		prev_ptr = self.head

		i = 2
		while( ptr != None ):
			if i == number_of_node:
				return (ptr,prev_ptr)
			prev_ptr = ptr
			ptr = ptr.next
			i = i+1
		return (ptr,prev_ptr)

	# Function to find Location by data value in unsorted
	def find_loc_by_value_unsorted(self,data_value):
		# List is empty
		if self.head == None:
			return (None,None)

		ptr = self.head
		prev_ptr = None

		while(ptr != None):
			if data_value == ptr.data:
				return (ptr,prev_ptr)
			prev_ptr = ptr
			ptr=ptr.next
		return (ptr,prev_ptr)

	# Function to find Location by data value in sorted
	def find_loc_by_value_sorted(self,data_value):
		# List is empty
		if self.head == None:
			return (None,None)
		# Entered value is bigger than very first value in List
		if self.head.data < data_value:
			return (None,None)

		ptr = self.head
		prev_ptr = None

		while(ptr != None and data_value <= ptr.data):
			if data_value == ptr.data:
				return (ptr,prev_ptr)
			prev_ptr = ptr
			ptr=ptr.next
		return (None,None)

	#Function to delete after some Location
	def delete(self,ptr,prev_ptr):
		if ptr == None:
			print "Node not found!"
		elif prev_ptr == None:
			self.head = self.head.next
		else:
			prev_ptr.next = ptr.next

	# Function to print the LinkedList
	def printList(self):
		ptr = self.head
		while(ptr):
			print ptr.data,
			ptr = ptr.next

if __name__ == '__main__':
	llist = LinkedList()

	llist.push(15)
	llist.push(16)
	llist.push(17)
	llist.push(14)
	llist.push(13)



	print "Original LinkedList"
	llist.printList()

	number_of_node = int(raw_input("\nAt which place you want to delete? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	(ptr,prev_ptr) = llist.find_loc_by_number(int(number_of_node))
	llist.delete(ptr,prev_ptr)


	print "\nOriginal LinkedList"
	llist.printList()

	data_value = int(raw_input("\n\nWhich data you want to delete? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	(ptr,prev_ptr) = llist.find_loc_by_value_unsorted(data_value)
	llist.delete(ptr,prev_ptr)


	print "\nOriginal LinkedList"
	llist.printList()

	data_value = int(raw_input("\n\nWhat data you want to delete? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	(ptr,prev_ptr) = llist.find_loc_by_value_sorted(data_value)
	llist.delete(ptr,prev_ptr)

	print "\nOriginal LinkedList"
	llist.printList()
		
		