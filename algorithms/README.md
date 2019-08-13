# Algorithms

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
        a, b = b, a%b
    return a

def gcd_recursive(a, b):
    """Calculate the Greatest Common Divisor of a and b recursive.
    """
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

## Recursion

When a function calls itself

- Make sure that your recursive function has a breaking condition, so that it terminates without an infinite loop 
- Each time the function is called, the old arguments are saved in the **call stack**

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Sorting Data

Type | Runtime
-----|---------
Bubble sort | O(n^2)
Merge sort  | O(n log n)
Quick sort  | O(n log n)

**Bubble sort:**

The bubble sort algorithm traverses the array and compares the first 2 elements. It swaps them if the second element is larger. This continues till the end of the array. The larger values "bubble" their way to the top of the array. After the first traversal through the array, the process is repeated up to the second last element of the array.

- Very simple to understand and implement
- Has O(n^2) which is inefficient
    - For loops inside of for loops is usually O(n^2)
- Other sorting algorithms are much better


```python
# O(n^2)
def bubble_sort(items):
    for i in range(len(items) - 1, 0, -1):
        for j in range(i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(items)
print(bubble_sort(items))
```

**Merge sort:**

- A divide-and-conquer algorithm
- Breaks a data set into individual pieces and merges them
- Uses **recursion** to operate on the input
- Break the array down to single element arrays and merge them back together while sorting

```python
# O(n log n)
def merge_sort(items):
    if len(items) < 2:
        return

    # Split the array and call merge_sort
    mid = len(items) // 2
    left_side = items[:mid]
    right_side = items[mid:] 

    merge_sort(left_side)
    merge_sort(right_side)

    # Set the indexes for the 3 arrays
    i = j = k = 0

    # While both arrays have items
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            items[k] = left_side[i]
            i += 1
        else:
            items[k] = right_side[j]
            j += 1
        k += 1

    # Add left side values if any are remaining
    while i < len(left_side):
        items[k] = left_side[i]
        i += 1
        k+= 1

    # Add right side values if any are remaining
    while j < len(right_side):
        items[k] = right_side[j]
        j += 1
        k+= 1

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(items)
merge_sort(items)
print(items)
```

**Quick sort:**

- A divide-and-conquer algorithm like **merge sort**
- Breaks a data set into individual pieces and merges them
- Uses **recursion** to operate on the input
- Generally performs better than merge sort, O(n log n)
- Operates in place on data
- Worst case is O(n2) when data is mostly sorted already

```python
# O(n log n)
def quick_sort(items):
    pivot = items[0]

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(items)
print(merge_sort(items))
print(items)
```

## Searching Data

Searching an unordered list is O(n), linear time complexity.

```python
# O(n)
def search(val, items):
    for index, item in enumerate(items):
        if item == val:
            return index

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(search(87, items))   #=> 6
print(search(250, items))  #=> None
```

With a sorted list you can do a **Binary search:**

```python
# O(log n)
def binary_search(val, items):
    lower = 0
    upper = len(items) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if items[mid] == val:
            return mid

        if val > items[mid]:
            lower = mid + 1
        else:
            upper = mid - 1

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
print(binary_search(20, items))   #=> 3
print(binary_search(87, items))   #=> 9
print(binary_search(250, items))  #=> None
```

You can also determine if a list is sorted:

```python
# Brute force O(n)
def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

# Brute force using Python comprehension O(n)
def is_sorted(items):
    return all(items[i] <= items[i+1] for i in range(len(items)-1))

# Binary search O(log n)
def is_sorted(items):
    lower = 0
    upper = len(items) - 1

    while lower <= upper:
        if items[lower] > items[upper]:
            return False
        lower += 1
        upper -= 1

    return True

unsorted = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
sorted = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
print(is_sorted(unsorted))  #=> True
print(is_sorted(sorted))    #=> False
```

```python
def max(items):
    if not items:
        return 0

    first = items[0]
    if len(items) < 2
        return first

    remaining = items[1:]
    if first > items[1]:
        return max([first] + items[2:])
    else:
        return max(remaining)
```

## Resources

- https://www.linkedin.com/learning/programming-foundations-algorithms/algorithms-power-the-world
