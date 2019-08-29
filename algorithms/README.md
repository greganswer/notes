# Algorithms

An algorithm is a series of steps to solve a problem. An algorithm can use 0 or more data structures. 
A good algorithm is readable (by humans) and scalable (by machines).

### Characteristics

The 3 pillars of good code:
1. Readable
2. Time Complexity
3. Space Complexity

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

### Measuring algorithms with Big O

Big-O notation

- A measure of the longest amount of time it could possibly take for the algorithm to complete.
- Determine the performance of an algorithm as the input size grows
- `O()` indicates the **order of operation**: time scale to perform an operation
- Many algorithms and data structures have more than one `O()`
    - Create/Read/Update/Delete of data
- This calculates the number of operations. 7 operations is `O(7)`. We always simplify to `O(1)`

#### Notations

**Big-O** is a measure of the longest amount of time it could possibly take for the algorithm to complete.
`f(n) ≤ cg(n)`, where `f(n)` and `g(n)` are non-negative functions, `g(n)` is upper bound, then `f(n)` 
is Big O of `g(n)`. This is denoted as `f(n) = O(g(n))`.

**Big Omega** describes the best that can happen for a given data size.
`f(n) ≥ cg(n)`, this makes `g(n)` a lower bound function

**Theta** is basically saying that the function, f(n) is bounded both from the top and bottom by the same function, `g(n)`.
f(n) is theta of `g(n)` if and only if `f(n) = O(g(n))` and `f(n) = Ω(g(n))`
This is denoted as `f(n) = Θ(g(n))`. 

| Notation   | Description                                       | Example                                                                                          |
| ---------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| O(1)       | Constant time. Independent of data set. No loops. | Looking up a single element in an array                                                          |
| O(log n)   | Logarithmic                                       | Finding an item in a sorted array with a binary search                                           |
| O(n)       | Linear time                                       | Loops. Searching an unsorted array for a specific value                                          |
| O(n log n) | Log-linear                                        | Complex sorting algorithms like heap sort and merge sort                                         |
| O(n^2)     | Quadratic                                         | Nested loops. Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort |
| O(2^n)     | Exponential                                       | Recursive algorithms that solves a problem of size N                                             |
| O(n!)      | Factorial                                         | Adding a loop for every element                                                                  |

#### Rules for calculation

1. Always describe the worst case scenario
2. Remove constants from the equation
3. Different inputs should have different variables. `O(a+b)` for steps in order. A and B arrays nested would be `O(a*b)`.
4. Drop Non-dominant terms

#### Space complexity

- Space complexity refers to how much additional space the algorithm requires to execute (independent of space required for it's inputs)
- Programs store data in the `heap` or the `stack`
    - The `heap` is where variables are stored
    - The `stack` is where function calls are stored
- What causes space complexity
    - Variables
    - Data Structures
    - Function calls
    - Allocations

## Sorting Data

| Type        | Runtime    |
| ----------- | ---------- |
| Bubble sort | O(n^2)     |
| Merge sort  | O(n log n) |
| Quick sort  | O(n log n) |

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

## Misc

### Fizz buzz

```python
# Write a program that prints the numbers from 1 to 100. But for multiples of 
# 3 print "Fizz" instead of the number and for the multiples of 5 print "Buzz". 
# For numbers which are multiples of both 3 and 5 print "FizzBuzz".
def fizz_buzz():
    """
    Time - O(n)
    """
    for i in range(1, 101):
        output = "fizz" if (i % 3) == 0 else ""
        output += "buzz" if (i % 5) == 0 else ""
        print(output if output else i)


fizz_buzz()
```

### Log all pairs

```python
def log_all_pairs(items):
    """ Print out all the unique pairs based on the list of items.
    Time - O(n)
    """
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            print(items[i], items[j])


log_all_pairs([1, 2, 3, 4, 5])
```

## Resources

- https://www.linkedin.com/learning/programming-foundations-algorithms/algorithms-power-the-world
