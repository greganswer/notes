# Recursion examples

All examples below are written in Python. In Ruby, substitute the `if` `else` 
statement with a ternary operator.

## Powers

Write a function that returns the results for `num` to the power of `pwr`.

```python
def power(num, pwr):
    return num if pwr < 2 else num * power(num, pwr-1)

print(power(2, 4))  #=> 2x2x2x2 == 32
```

## Factorial

Write a function that returns the factorial of `n`. The factorial of a positive 
integer `n`, denoted by `n!`, is the product of all positive integers less than 
or equal to `n`.

```python
def factorial(num):
    return 1 if num < 2 else num * factorial(num-1)

print(factorial(5))  #=> 5x4x3x2x1 == 120
```

## Fibonacci

Write a function that returns the fibonacci when given input `num`.

```python
def fibonacci(num):
    return num if num < 2 else fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(5))  #=> 32
```