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

	# Function to find Location by number of node
	# if number is more than length of List, location of last node will be retrned
	def find_loc_by_number(self,number_of_node):
		# List is empty
		if self.head == None:
			return None

		if number_of_node == 1:
			return None

		ptr = self.head

		i = 2
		while ptr != None:
			if i == number_of_node:
				return ptr
			prev_ptr = ptr
			ptr = ptr.next
			i = i+1
		return prev_ptr

	# Function to find Location by data value in unsorted
	# if number is not in List, location of last node will be retrned
	def find_loc_by_value_unsorted(self,data_value):
		# List is empty
		if self.head == None:
			return None

		ptr = self.head

		while ptr != None:
			if data_value == ptr.data:
				return ptr
			prev_ptr = ptr
			ptr=ptr.next
		return prev_ptr

	# Function to find Location by data value in sorted
	def find_loc_by_value_sorted(self,data_value):
		# List is empty
		if self.head == None:
			return None
		# Entered value is bigger than very first value in List
		if self.head.data < data_value:
			return None

		ptr = self.head.next
		prev_ptr = self.head

		while ptr != None:
			if data_value > ptr.data:
				return prev_ptr
			prev_ptr = ptr
			ptr=ptr.next
		return prev_ptr

	#Function to insert after some Location
	def insert(self,ptr,new_data):
		if ptr == None:
			self.push(new_data)
		else:
			new_node = Node(new_data)
			new_node.next = ptr.next
			ptr.next = new_node

	# Function to print the LinkedList
	def printList(self):
		ptr = self.head
		while ptr:
			print ptr.data,
			ptr = ptr.next

if __name__ == '__main__':
	llist = LinkedList()

	llist.push(15)
	llist.push(16)
	llist.push(17)


	print "Original LinkedList"
	length = llist.printList()

	number_of_node = int(raw_input("\nAt which place you want to insert? : "))
	new_data = int(raw_input("\nWhat data you want to insert? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	llist.insert(llist.find_loc_by_number(int(number_of_node)),new_data)


	print "\nOriginal LinkedList"
	llist.printList()

	data_value = int(raw_input("\n\nAfter which data you want to insert? : "))
	new_data = int(raw_input("\nWhat data you want to insert? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	llist.insert(llist.find_loc_by_value_unsorted(data_value),new_data)


	print "\nOriginal LinkedList"
	llist.printList()

	new_data = int(raw_input("\n\nWhat data you want to insert? : "))
	# print llist.find_loc_by_number(int(number_of_node))
	llist.insert(llist.find_loc_by_value_sorted(new_data),new_data)

	print "\nOriginal LinkedList"
	llist.printList()
		
		