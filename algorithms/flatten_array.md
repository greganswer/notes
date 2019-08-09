# Flatten array

Given the following input:

    [1, [2, 3, [4, 5], 6], 7, [8]]

Write a function to produce the following output:

    [1, 2, 3, 4, 5, 6, 7, 8]

**Ruby implementation:**

```ruby
def flatten(items)
  first = items[0]
  remaining = items[1..-1]
  output = first.is_a?(Array) ? flatten(first) : [first]
  output += flatten(remaining) if remaining.any?
  output
end
```

**Python implementation:**

```python
def flatten(items):
    first = items[0]
    remaining = items[1:]
    output = flatten(first) if type(first) is list else [first]
    if len(remaining):
        output += flatten(remaining)
    return output
```
