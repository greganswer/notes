# Search

- [Summary](#summary)
- [Details](#details)
  - [Linear search](#linear-search)
  - [Binary search](#binary-search)
  - [Breadth first search (BFS)](#breadth-first-search-bfs)
    - [Dijkstra vs. Bellman](#dijkstra-vs-bellman)
  - [Depth first search (DFS)](#depth-first-search-dfs)
    - [Pre order traversal](#pre-order-traversal)
    - [In order traversal](#in-order-traversal)
    - [Post order traversal](#post-order-traversal)
- [Examples](#examples)
  - [Depth first search traversal comparison](#depth-first-search-traversal-comparison)
- [References](#references)

## Summary

## Details

### Linear search

- Sequentially search each element until item is found
- Time - Average and worst case scenario is `O(n)` linear 

```python
def linear_search(val, items)
    for index, item in enumerate(items):
        if item == val:
            return index
```

### Binary search

- With a sorted list you can do a binary search
- Time - Average is `O(log n)` logarithmic and worst case is `O(n)` linear 
    - Sorted graphs and trees have a `O(log n)` logarithmic search time complexity whereas lists and hash tables have a `O(n)` linear search time complexity
    - Time complexity to search all nodes is `O(n)` linear

```python
def binary_search(val, items)
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
```

### Breadth first search (BFS)

- Traverse the data structure from left to right
- Uses additional memory because you have to store the parent node of all the child nodes

| Advantages                        | Disadvantages |
| --------------------------------- | ------------- |
| Shortest path                     | More memory   |
| Closer nodes (most related items) |               |
| Good if the node is near the top  |               |
| Good for deep trees               |               |


```python
from collections import deque

def breadth_first_search(tree):
    values = []
    queue = deque()
    queue.append(tree.root_node)
    while len(queue):
        current_node = queue.popleft()
        values.append(current_node.value)
        left_node = current_node.left_node
        right_node = current_node.right_node
        if left_node is not None:
            queue.append(left_node.value)
        if right_node is not None:
            queue.append(right_node.value)
    return values
```

#### Dijkstra vs. Bellman

- Bellman's Breadth first search algorithm 
    - Is better than Dijkstra's because it can accommodate negative weights
    - Is slower than Dijkstra's, with a `O(n^2)` quadratic time complexity

### Depth first search (DFS)

- Traverse the data structure all the way down the left then again all the way down the right
- Space - `O(depth_of_tree)`, due to recursive calls

| Advantages                  | Disadvantages |
| --------------------------- | ------------- |
| Less memory                 | Can be slower |
| Does the path exist?        |               |
| Can be used to solve a maze |               |
| Good for wide trees         |               |


**Note:** The following examples use this tree as input:

            9
         4     20
       1  6  15  170


#### Pre order traversal

- Start with the root node and then traverse the leftmost children, then it's sibling to the right, then it's parent's sibling, then it's children left to right
- Useful for when you want to recreate a tree

Result:

      [9, 4, 1, 6, 20, 15, 170]

#### In order traversal

- Start at the leftmost leaf and proceed in ascending order of node value

Result:

      [1, 4, 6, 9, 15, 20, 170]

#### Post order traversal

- Start with the leftmost leafs and work your way up to the parents

Result:

      [1, 6, 4, 15, 170, 20, 9]

## Examples

### Depth first search traversal comparison

**IMPORTANT:** Notice that the type of ordering determines when the node gets appended to the list.

```python
def dfs_pre_order(node, list):
    list.append(node.value)
    if node.left_node is not None:
        dfs_pre_order(node.left_node, list)
    if node.right_node is not None:
        dfs_pre_order(node.right_node, list)

def dfs_in_order(node, list):
    if node.left_node is not None:
        dfs_in_order(node.left_node, list)
    list.append(node.value)
    if node.right_node is not None:
        dfs_in_order(node.right_node, list)
  

def dfs_post_order(node, list):
    if node.left_node is not None:
        dfs_post_order(node.left_node, list)
    if node.right_node is not None:
        dfs_post_order(node.right_node, list)
    list.append(node.value)
``` 

```python
# Replace `traverse` with the name of the actual function above.
traverse(tree.root_node, [])
```

## References

- https://stackoverflow.com/questions/9844193/what-is-the-time-and-space-complexity-of-a-breadth-first-and-depth-first-tree-tr