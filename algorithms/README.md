# Algorithms

- [Summary](#summary)
- [Details](#details)
  - [Common algorithms](#common-algorithms)
  - [Measuring algorithms with Big O](#measuring-algorithms-with-big-o)
    - [Notations](#notations)
    - [Rules for calculation](#rules-for-calculation)
    - [Space complexity](#space-complexity)
  - [Dynamic programming](#dynamic-programming)
- [Examples](#examples)
  - [Fizz buzz](#fizz-buzz)
  - [Log all pairs](#log-all-pairs)
- [References](#references)

## Summary

An algorithm is a series of steps to solve a problem. An algorithm can use 0 or more data structures. 
A good algorithm is readable (by humans) and scalable (by machines).

## Details

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

### Dynamic programming

- Just a buzz word for caching
- Caching is just a way to store values so you can use them later
- **Memoization:** an optimization technique to store the results of expensive function calls and return the cached result when the same inputs occur again
- Can be used when:
    - The problem can be divided into subproblems
    - The solution is recursive

## Examples

### Fizz buzz

```python
def fizz_buzz():
    """
    Write a program that prints the numbers from 1 to 100. But for multiples of 
    3 print "Fizz" instead of the number and for the multiples of 5 print "Buzz". 
    For numbers which are multiples of both 3 and 5 print "FizzBuzz".

    Time - O(1): Only done for 100 integers.
    Space - O(1): Only 1 string variable with a max length of 8 for "fizzbuzz".
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
    """ 
    Print out all the unique pairs based on the list of items.

    Time - O(n^2): Nested for loop over the items.
    Space - O(1): No new variables introduced.
    """
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            print(items[i], items[j])


log_all_pairs([1, 2, 3, 4, 5])
```

## References

- https://www.linkedin.com/learning/programming-foundations-algorithms/algorithms-power-the-world
