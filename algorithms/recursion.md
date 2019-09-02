# Recursion

- [Summary](#summary)
- [Details](#details)
- [Examples](#examples)
  - [Powers](#powers)
  - [Factorial](#factorial)
  - [Fibonacci](#fibonacci)
- [References](#references)

## Summary

| Advantages           | Disadvantages             |
| -------------------- | ------------------------- |
| Easier to read/write | More memory on call stack |

## Details

When a function calls itself.

- Make sure that your recursive function has a breaking condition, so that it terminates without an infinite loop 
- Each time the function is called, the old arguments are saved in the **call stack**
- The computer needs to allocate memory for each function call (this is known as the stack)
- Stack Overflow is when there are too many functions that have not been popped off the call stack yet
- Each recursive function has the following:
    - The base case: The situation when the function terminates
    - The recursive case: The situation when the function calls itself
- Best situations to use recursion:
    - When traversing trees
    - When solving a problem using divide and conquer (divide a problem into smaller problems and merge the solutions back together)
- Recursion can be easier to read and write but it comes at an increased space complexity

## Examples

### Powers

Write a function that returns the results for `num` to the power of `pwr`.

```python
def power(num, pwr):
    """
    Time - O(n) linear, where n is the integer passed in.
    Space - O(n) linear, where n is the integer passed in, which is also the number of 
            times power is added to the call stack.
    """
    return num if pwr < 2 else num * power(num, pwr-1)

print(power(2, 4))  #=> 2x2x2x2 == 32
```

### Factorial

Write a function that returns the factorial of `n`. The factorial of a positive 
integer `n`, denoted by `n!`, is the product of all positive integers less than 
or equal to `n`.

```python
def factorial(num):
    """
    Time - O(n) linear, where n is the integer passed in.
    Space - O(n) linear, where n is the integer passed in, which is also the number of 
            times factorial is added to the call stack.
    """
    return 1 if num < 2 else num * factorial(num-1)

def factorial_iterative(num):
    """
    Time - O(n) linear, where n is the integer passed in.
    Space - O(1) constant, for the variable named output.
    """
    output = 1
    for i in range(2, num + 1):
        output *= i
    return output

print(factorial(5))  #=> 5x4x3x2x1 == 120
```

### Fibonacci

Write a function that returns the fibonacci when given input `num`.

```python
def fibonacci(num):
    """
    Brute Force: Recursion

    Time - O(2^n) exponential, where n is the integer passed in.
    Space - O(n) linear, where n is the integer passed in, which is also the number of 
            times fibonacci is added to the call stack.
    """
    if num < 1:
        return 0
    if num < 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)
```

```python
def fibonacci(num: int) -> int:
    """
    Iteratively:

    Time - O(n) linear, where n is the integer passed in.
    Space - O(n) linear, where n is the integer passed in, which is also the number of 
            times num is added to the output list.
    """
    if num < 1:
        num = 0
    output = [0, 1]
    for i in range(2, num + 1):
        output.append(output[i-2] + output[i-1])
    return output[num]
```

```python
def fibonacci(num, memo={}):
    """
    Dynamic Programming: Memoization and recursion

    Time - O(n) linear, where n is the integer passed in.
    Space - O(n) linear, where n is the integer passed in, which is also the number of 
            times num is added to the memo dictionary.
    """
    if num < 1:
        return 0
    if num < 2:
        return 1
    if memo.get(num) is not None:
        return memo[num]
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]

print(fibonacci(5))  #=> 32
```

```python
def fibonacci(num):
    """
    Using 3 variables:

    Time - O(n) linear, where n is the integer passed in.
    Space - O(1) constant, because only 3 integers are created inside the function.
    """
    if num < 1:
        return 0
    if num < 2:
        return 1
    previous = output = 0
    current = 1
    for i in range(2, num + 1):
        output = previous + current
        previous = current
        current = output
    return output
```

## References