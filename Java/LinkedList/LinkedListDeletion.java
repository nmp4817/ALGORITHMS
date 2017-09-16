import java.util.Scanner;

public class LinkedListDeletion {
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
		push(14);
		push(13);

		printList();

		Scanner scan = new Scanner(System.in);

		System.out.println("\n\nAt which place you want to delete? : ");
		int number_of_node = scan.nextInt();
		ResultType r = find_loc_by_number(number_of_node);
		delete(r.ptr,r.prev_ptr);
		printList();

		System.out.println("\n\nWhat number you want to delete? : ");
		int data_value = scan.nextInt();
		r = find_loc_by_value_unsorted(data_value);
		delete(r.ptr,r.prev_ptr);
		printList();

		System.out.println("\n\nWhat data you want to delete? : ");
		data_value = scan.nextInt();
		r = find_loc_by_value_unsorted(data_value);
		delete(r.ptr,r.prev_ptr);
		printList();

	}

	public static void push (int data) {
		Node new_node = new Node(data);
		new_node.next = LinkedListDeletion.head;
		LinkedListDeletion.head = new_node;
	}

	public static ResultType find_loc_by_number(int number_of_node) {
		// List is empty
		if (LinkedListDeletion.head == null ) return new ResultType(null,null);

		if ( number_of_node == 1 ) return new ResultType(LinkedListDeletion.head,null);


		Node ptr = LinkedListDeletion.head.next;
		Node prev_ptr = LinkedListDeletion.head;

		int i = 2;

		while( ptr != null ) {
			if ( i == number_of_node ) return new ResultType(ptr,prev_ptr);
			prev_ptr = ptr;
			ptr = ptr.next;
			i = i+1;
		}
		return new ResultType(ptr,prev_ptr);
	}

	public static ResultType find_loc_by_value_unsorted(int data_value) {
		// List is empty
		if ( LinkedListDeletion.head == null )	return new ResultType(null,null);

		Node ptr = LinkedListDeletion.head;
		Node prev_ptr = null;

		while ( ptr != null ) {
			if ( data_value == ptr.data ) return new ResultType(ptr,prev_ptr);
			prev_ptr = ptr;
			ptr=ptr.next;
		}
		return new ResultType(ptr,prev_ptr);
	}

	public static ResultType find_loc_by_value_sorted(int data_value) {
		// List is empty
		if ( LinkedListDeletion.head == null )	return new ResultType(null,null);
		// Entered value is bigger than very first value in List
		if ( LinkedListDeletion.head.data < data_value ) return new ResultType(null,null);

		Node ptr = LinkedListDeletion.head;
		Node prev_ptr = null;

		while ( ptr != null && data_value <= ptr.data) {
			if ( data_value > ptr.data ) return new ResultType(ptr,prev_ptr);
			prev_ptr = ptr;
			ptr=ptr.next;
		}

		return new ResultType(null,null);
	}

	public static void delete(Node ptr,Node prev_ptr) {
		if ( ptr == null ) System.out.println("\nNode not found!");
		else if ( prev_ptr == null ) LinkedListDeletion.head = LinkedListDeletion.head.next;
		else prev_ptr.next = ptr.next;
	}

	public static void printList() {
		Node ptr = LinkedListDeletion.head;
		while ( ptr != null ) {
			System.out.print(""+ptr.data+" ");
			ptr = ptr.next;
		}
	}

}

class ResultType {
	LinkedListDeletion.Node ptr,prev_ptr;
	ResultType(LinkedListDeletion.Node ptr,LinkedListDeletion.Node prev_ptr) {
		this.ptr = ptr;
		this.prev_ptr = prev_ptr;
	}
}