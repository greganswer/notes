# Flatten array

Given the following input:

    [1, [2, 3, [4, 5], 6], 7, [8]]

Write a function to produce the following output:

    [1, 2, 3, 4, 5, 6, 7, 8]

## Recursive

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
    output = flatten(first) if isinstance(first, list) else [first]

    if len(remaining):
        output += flatten(remaining)
    return output
```

## Iterative

**NOTE:** Popping the first element off of an array/list has bad performance
because all the elements have to be shifted. This is for learning purposes only.
Use a more efficient data structure like a linked list or Python's `deque`.

**Ruby implementation:**

```ruby
def flatten(items)
  output = []
  while items.length > 0
    item = items.shift
    if item.is_a?(Array) && item.size > 0
      first = item.shift
      items.unshift(first, item)
    else
      output << item unless item == []
    end
  end
  output
end
```

**Python implementation:**

```python
def flatten(items):
    output = []
    while len(items):
        item = items.pop(0)
        if isinstance(item, list) and len(item):
            items.insert(0, item.pop(0))
            if len(item):
                items.insert(1, item)
        else:
            output.append(item)
    return output
```
