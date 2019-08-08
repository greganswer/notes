# Algorithms

## Overview

### Characteristics

Algorithm complexity

- **Space complexity:** How much memory does it require?
- **Time complexity:** How much time does it require? How efficient is the algorithm relative to the size of the inputs?

Inputs and outputs

- What does the algorithm accept and what are the results?

Classification

- **Serial** (sequential) vs. **parallel** (break up a data set into smaller pieces and work on them individually)
- **exact** (produces a known predictable value) vs. **approximate** (e.g: a facial recognition algorithm may give different answers)
- **deterministic** (execute each step with an exact decision) vs. **non-deterministic** (produce a solution using guesses that become more accurate over time)

### Common algorithms

Search algorithms

- Find specific data in a structure
- E.g: find a substring within a string
- E.g: find a file in a folder

Sorting algorithms

- Take a set of data and place it into a particular order

Computational algorithms

- Use one set of data to derive another set of data from it
- Is a given number prime?
- Convert Fahrenheit to Celsius 

Collection algorithms

- Work with collections of data
- E.g: count specific items, traverse the items, filter out unwanted items, etc.

Greatest common denominator (GCD) of 2 integers.

Example: GCD of 20 and 8 is 4 (because 8/4 is 2 and 20/4 is 5)

1. For 2 integers `a` and `b`, where `a` > `b`, divided `a` by `b`.
1. If the remainder, `r`, is 0, then stop. GCD is `b`.
1. Otherwise, set `a`, to `b`, `b` to `r` and repeat at step 1 until `r is 0.

```python
# Theses algorithms are sequential, exact, and deterministic
def gcd_iterative(a, b):
    """Calculate the Greatest Common Divisor of a and b iteratively.
    """
    while b:
        print(f'a={a}; b={b}; a%b={a%b}')
        a, b = b, a%b
    return a

def gcd_recursive(a, b):
    """Calculate the Greatest Common Divisor of a and b recursive.
    """
    print(f'a={a}; b={b}; a%b={a%b}')
    if a % b == 0:
        return b
    return gcd_recursive(b, a%b)
```

### Measuring algorithms

Big-O notation

- Determine the performance of an algorithm as the input size grows
- "O" indicates the **order of operation**: time scale to perform an operation
- Many algorithms and data structures have more than one O
    - Create/Read/Update/Delete of data

Notation   | Description                                     | Example
-----------|-------------------------------------------------|---------
O(1)       | Constant time. Does not depend on the data set. | Looking up a single element in an array
O(log n)   | Logarithmic       | Finding an item in a sorted array with a binary search
O(n)       | Linear time       | Searching an unsorted array for a specific value
O(n log n) | Log-linear        | Complex sorting algorithms like heap sort and merge sort
O(n^2)     | Quadratic         | Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort

## Common data structures

Data structures are used to organize data so it can be processed.

Examples:
- Task list
- Directory tree structure

### Arrays

- A collection of elements identified by index or key
- A one dimensional array is just a list of items
- A two dimensional array is a list of lists of items

Description | Time Index
------------|---------------
Calculating item index                                            | O(1)
Insert or delete at beginning <br>(remaining items must be moved) | O(n)
Insert or delete in middle <br>(same as above)                    | O(n)
Insert or delete at the end                                       | O(1)

### Linked lists

- A linear collection of data elements, called nodes
- Similar to an array but a bit different
- **Each node has field that points to the next element in the list**
- Each element holds whatever data the application needs
- First item in the list is known as **the head**
- Last item in the list points to null, which means it's the end of the list

Add/Remove

- To add an item to the beginning of the list set the new node's `next` pointer to `head`, and set `head` to the new node
- To delete item 3 from a 4 item list, set the `previous` pointer for item 4 to item 2, set the `next` pointer for item 2 to item 4

Singly linked list diagram
![Singly linked list](/images/singly_linked_list.png)

Doubly linked list diagram. Each element also knows about it's previous element.
![Doubly linked list](/images/doubly_linked_list.png)

Advantages

- Linked lists can add/remove items faster than arrays
- Underlying memory doesn't need to be reorganized

Disadvantages

- Can't do constant-time random item access like any item in an array
- Item lookup is linear in time complexity (O(n))

### Stacks and queues

### Trees

### Hash tables

## Recursion

## Sorting Data

## Searching Data

## Resources

- https://www.linkedin.com/learning/programming-foundations-algorithms/algorithms-power-the-world
