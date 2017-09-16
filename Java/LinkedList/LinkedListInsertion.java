import java.util.Scanner;

public class LinkedListInsertion {
	static Node head;
	static class Node {
		int data;
		Node next;

		Node(int data) {
			this.data = data;
			this.next = null; 
		}
	}

	public static void main(String[] args) {
		// Node head = new Node(17);
		// Node second = new Node(16);
		// Node third = new Node(15);

		// head.next = second;
		// second.next = third;
		// third.next = null;
		push(15);
		push(18);
		push(20);

		printList();

		Scanner scan = new Scanner(System.in);

		System.out.println("\n\nAt which place you want to insert? : ");
		int number_of_node = scan.nextInt();
		System.out.println("What number you want to insert? : ");
		int new_data = scan.nextInt();
		insert(find_loc_by_number(number_of_node),new_data);
		printList();

		System.out.println("\n\nAfter which data you want to insert? : ");
		int data_value = scan.nextInt();
		System.out.println("What number you want to insert? : ");
		new_data = scan.nextInt();
		insert(find_loc_by_value_unsorted(data_value),new_data);
		printList();

		System.out.println("\n\nWhat data you want to insert? : ");
		new_data = scan.nextInt();
		insert(find_loc_by_value_sorted(new_data),new_data);
		printList();

	}

	public static void push (int data) {
		Node new_node = new Node(data);
		new_node.next = LinkedListInsertion.head;
		LinkedListInsertion.head = new_node;
	}

	public static Node find_loc_by_number(int number_of_node) {
		// List is empty
		if (LinkedListInsertion.head == null ) return null;

		if ( number_of_node == 1 ) return null;


		Node ptr = LinkedListInsertion.head;
		Node prev_ptr = null;

		int i = 2;

		while( ptr != null ) {
			if ( i == number_of_node ) return ptr;
			prev_ptr = ptr;
			ptr = ptr.next;
			i = i+1;
		}
		return prev_ptr;
	}

	public static Node find_loc_by_value_unsorted(int data_value) {
		// List is empty
		if ( LinkedListInsertion.head == null )	return null;

		Node ptr = LinkedListInsertion.head;
		Node prev_ptr = null;

		while ( ptr != null ) {
			if ( data_value == ptr.data ) return ptr;
			prev_ptr = ptr;
			ptr=ptr.next;
		}
		return prev_ptr;
	}

	public static Node find_loc_by_value_sorted(int data_value) {
		// List is empty
		if ( LinkedListInsertion.head == null )	return null;
		// Entered value is bigger than very first value in List
		if ( LinkedListInsertion.head.data < data_value ) return null;

		Node ptr = LinkedListInsertion.head.next;
		Node prev_ptr = LinkedListInsertion.head;

		while ( ptr != null ) {
			if ( data_value > ptr.data ) return prev_ptr;
			prev_ptr = ptr;
			ptr=ptr.next;
		}

		return prev_ptr;
	}

	public static void insert(Node ptr,int new_data) {
		if ( ptr == null ) push(new_data);
		else {				
			Node new_node = new Node(new_data);
			new_node.next = ptr.next;
			ptr.next = new_node;
		}
	}

	public static void printList() {
		Node ptr = LinkedListInsertion.head;
		while ( ptr != null ) {
			System.out.print(""+ptr.data+" ");
			ptr = ptr.next;
		}
	}

}