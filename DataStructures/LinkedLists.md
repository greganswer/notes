# Linked lists

- A linear collection of data elements, called nodes
- Similar to an array but a bit different
- **Each node has a field that points to the next element in the list**
- Each element holds whatever data the application needs
- First item in the list is known as the **head** and the last is the **tail**
- Last item in the list points to null, which means it's the end of the list
- They can be used to create other data structures: **stacks, queues, etc.**

## Adding and removing

- To add an item to the beginning of the list set the new node's `next` pointer to `head`, and set `head` to the new node
- To delete item 3 from a 4 item list, set the `previous` pointer for item 4 to item 2, set the `next` pointer for item 2 to item 4

Singly linked list diagram
![Singly linked list](/images/singly_linked_list.png)

Doubly linked list diagram. Each element also knows about it's previous element.
![Doubly linked list](/images/doubly_linked_list.png)

## Advantages

- Linked Lists are dynamic data structures (can add/remove items faster than arrays)
- Memory is allocated at run time (underlying memory doesn't need to be reorganized)
- Can store items of different sizes (Arrays assume every element is the same size)

## Disadvantages

- Can't do constant-time random item access like any item in an array
- Wastes memory because of the references to other nodes
- Item lookup has an O(n) linear time complexity because items must be read in order
- Arrays use indexes which have an O(1) constant time complexity
- Singly Linked Lists are difficult to traverse in reverse
- Doubly Linked Lists waste additional memory

## Example
```python
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) time complexity: size is calculated on insert/delete and is cached.
    def __len__(self):
        return self.size

# Create
    # O(1) time complexity.
    def prepend(self, data):
        """Add a Node to the beginning of the LinkedList"""
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    # O(n) time complexity.
    def append(self, data):
        """Add a Node to the end of the LinkedList"""
        node = Node(data)
        current = self.head

        if self.head is None:
            self.prepend(data)
            return

        while current.next is not None:
            current = current.next
        current.next = node
        self.size += 1

# Read
    # O(n) time complexity.
    def display_nodes(self):
        output = ''
        current = self.head
        if current is None:
            return
        while current is not None:
            output += f'Node: {current.data}\n'
            current = current.next
        return output

# Delete
    # O(1) time complexity if the node is head. Otherwise O(n).
    def remove(self, data):
        """Remove a Node from the LinkedList"""
        current = self.head
        if current is None:
            return

        self.size -= 1

        if current.data == data:
            current = self.head.next
            return
        
        while current.next is not None:
            previous = current
            current = current.next
            if current.data == data:
                previous.next = current.next
        
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Instantiate
list = LinkedList()
print(f'Size: {len(list)}')  #=> 0

# Add
list.append(2)
list.append(3)
list.prepend(1)
print(f'Size: {len(list)}')  #=> 3
print()
print(list.display_nodes())  #=> Node: 1\n Node: 2\n Node: 3\n

# Remove
list.remove(2)
print(list.display_nodes())  #=> Node: 1\n Node: 3\n
print(f'Size: {len(list)}')  #=> 2
```