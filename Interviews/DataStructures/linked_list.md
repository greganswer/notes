# Linked lists

## Summary

- A data structure that represents a sequence of nodes
- A singly linked list, each node points to the next node in the linked list
- A doubly linked list gives each node pointers to both the next node and the previous node.
- Lookup is `O(n)` linear
- Adding/removing at the `head` or `tail` of the list has a of `O(1)`

## Details

- A Linked List is a type of **tree**, which is a type of **graph**
- A linear collection of data elements, called nodes
- Similar to an array but a bit different
- **Each node has a field that points to the next element in the list**
- Each element holds whatever data the application needs
- First item in the list is known as the **head** and the last is the **tail**
- Last item in the list points to null, which means it's the end of the list
- They can be used to create other data structures: **stacks, queues, etc.**

### Adding and removing

- To add an item to the beginning of the list set the new node's `next` pointer to `head`, and set `head` to the new node
- To delete item 3 from a 4 item list, set the `previous` pointer for item 4 to item 2, set the `next` pointer for item 2 to item 4

Singly linked list diagram
![Singly linked list](/images/singly_linked_list.png)
source: https://www.geeksforgeeks.org/data-structures/linked-list

Doubly linked list diagram. Each element also knows about it's previous element.
![Doubly linked list](/images/doubly_linked_list.png)
source: https://www.geeksforgeeks.org/doubly-linked-list/

### Advantages

- Linked Lists are dynamic data structures (can add/remove items faster than arrays)
- Memory is allocated at run time (underlying memory doesn't need to be reorganized)
- Can store items of different sizes (Arrays assume every element is the same size)

### Disadvantages

- Can't do constant-time random item access like any item in an array
- Wastes memory because of the references to other nodes
- Item lookup has an O(n) linear time complexity because items must be read in order
- Arrays use indexes which have an O(1) constant time complexity
- Singly Linked Lists are difficult to traverse in reverse but they take up a bit less memory
- With a Singly Linked List, insertion/deletion at the head/tail is fast
- Doubly Linked Lists waste additional memory
