# Data structures

Data structures are used to organize data so it can be processed.

Examples:
- Task list
- Directory tree structure

## Arrays

- A collection of elements identified by index or key
- A one dimensional array is just a list of items
- A two dimensional array is a list of lists of items

Description | Linked List<br>time complexity | Array<br>time complexity
------------|--------------------------------|---------------------------
Calculating item index                                             | O(n) | O(1)
Prepend item                                                       | O(1) | O(n)
Delete at the beginning/middle <br>(array items must be moved)     | O(1) | O(n)
Insert in the middle <br>(same as above)                           | O(n) | O(n)
Append                                                             | O(n) | O(n)
Delete at the end                                                  | O(n) | O(n)
Space waste                                                        | O(n) | 0

## Linked lists

- A linear collection of data elements, called nodes
- Similar to an array but a bit different
- **Each node has a field that points to the next element in the list**
- Each element holds whatever data the application needs
- First item in the list is known as the **head** and the last is the **tail**
- Last item in the list points to null, which means it's the end of the list
- They can be used to create other data structures: **stacks, queues, etc.**

Add/Remove

- To add an item to the beginning of the list set the new node's `next` pointer to `head`, and set `head` to the new node
- To delete item 3 from a 4 item list, set the `previous` pointer for item 4 to item 2, set the `next` pointer for item 2 to item 4

Singly linked list diagram
![Singly linked list](/images/singly_linked_list.png)

Doubly linked list diagram. Each element also knows about it's previous element.
![Doubly linked list](/images/doubly_linked_list.png)

Advantages

- Linked Lists are dynamic data structures (can add/remove items faster than arrays)
- Memory is allocated at run time (underlying memory doesn't need to be reorganized)
- Can store items of different sizes (Arrays assume every element is the same size)

Disadvantages

- Can't do constant-time random item access like any item in an array
- Wastes memory because of the references to other nodes
- Item lookup has an O(n) linear time complexity because items must be read in order
- Arrays use indexes which have an O(1) constant time complexity
- Singly Linked Lists are difficult to traverse in reverse
- Doubly Linked Lists waste additional memory

## Stacks and queues

Some languages have built in data types to represent these structures. 

**Stack:** 
- Collection that supports push and pop operations
- The last item pushed is the first one popped. Last In, First Out (LIFO)
- Pushing/popping an item on to the stack has a run time of O(1)
- Examples:
    - Processing a mathematical expression
    - Backtracking: browser back button

```python
# Add to stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  #=> [1, 2, 3]

# Pop off stack
item = stack.pop
print(stack)  #=> [1, 2]
```

**Queue:** 
- Collection that supports adding and removing
- The first item pushed is the first one popped. First In, First Out (FIFO)
- Pushing/popping an item on to the stack has a run time of O(1)
- Examples:
    - Order processing
    - Message processing

```python
from collections import deque

# Add to queue
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  #=> deque([1, 2, 3])

# Pop off queue
item = queue.popleft()
print(queue)  #=> deque([2, 3])
```

## Hash tables

- Also known as a dictionary or associative array
- Most languages have hash tables already implemented
- The most important thing is to under it's structure, as well as pros/cons
- It's a data structure that maps keys to their associated values
- It does this using a **hash function**
    - Uses the key to compute the index into the slots that are in the hash table
    - Ideally, each key is uniquely assigned to a value
    - Sometimes there are collisions

**Advantage:**
- Key-value mappings are unique
- They're typically faster than any other structure, especially with a large data set

**Drawbacks:**
- For small data sets, arrays are usually faster
- Hash tables order is not predictable

```python
hash = {"a": 1, "b": 2}
print(hash)  #=> {'a': 1, 'b': 2}

hash["c"] = "three"
print(hash)  #=> {'a': 1, 'b': 2, 'c': 'three'}

for key, val in hash.items():
    print(f'Key: {key}, Value {val}')
```

## Trees