Write a function that returns the fibonacci when given input `n`

**Ruby implementation:**

```ruby
def fibonacci(n)
  n < 2 ? n : fibonacci(n-1) + fibonacci(n-2)
end
```

**Python implementation:**

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```