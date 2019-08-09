# Recursion examples

## Powers

Write a function that returns the results for `num` to the power of `pwr`.

```python
power(2, 4)  #=> 2x2x2x2 == 32
```

**Python implementation:**

```python
def power(num, pwr):
    return num if pwr < 2 else num * power(num, pwr-1)
```

**Ruby implementation:**

```ruby
def power(num, pwr)
  pwr < 2 ? num : num * power(num, pwr-1)
end
```

## Factorial

```python
factorial(5)  #=> 5x4x3x2x1 == 120
```

**Python implementation:**

```python
def factorial(num):
    return 1 if num < 2 else num * factorial(num-1)
```

**Ruby implementation:**

```ruby
def factorial(num)
  num < 2 ? 1 : num * factorial(num-1)
end
```

## Fibonacci

Write a function that returns the fibonacci when given input `num`.

```python
fibonacci(5)  #=> 32
```

**Python implementation:**

```python
def fibonacci(num):
    return num if num < 2 else fibonacci(num-1) + fibonacci(num-2)
```

**Ruby implementation:**

```ruby
def fibonacci(num)
  num < 2 ? num : fibonacci(num-1) + fibonacci(num-2)
end
```
