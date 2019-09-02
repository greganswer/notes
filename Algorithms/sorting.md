# Sorting

- [Definitions](#definitions)
- [Which algorithm to use when](#which-algorithm-to-use-when)
- [Elementary sorting](#elementary-sorting)
  - [Bubble sort](#bubble-sort)
  - [Selection sort](#selection-sort)
  - [Insertion sort](#insertion-sort)
- [Divide and conquer sorting](#divide-and-conquer-sorting)
  - [Merge sort](#merge-sort)
  - [Quick sort](#quick-sort)
- [Non-comparison sort](#non-comparison-sort)
  - [Counting sort](#counting-sort)
  - [Radix sort](#radix-sort)
- [Determine if a list is sorted](#determine-if-a-list-is-sorted)
- [Sort algorithms per language](#sort-algorithms-per-language)
  - [Python](#python)
  - [Ruby](#ruby)
- [References](#references)

## Definitions

| Term                 | Definition                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **In-place sorting** | Modifies the given array only, so space use is constant                                                                 |
| **Internal sorting** | All data does not fid in memory. E.g: external storage like hard-disk, CD                                               |
| **External sorting** | All data is placed in-memory                                                                                            |
| **Stable sorting**   | if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted |

Stable Sorting Algorithms:
- Insertion Sort
- Merge Sort
- Bubble Sort
- Tim Sort
- Counting Sort
  
Unstable Sorting Algorithms:
- Heap Sort
- Selection sort
- Shell sort
- Quick Sort

## Which algorithm to use when

- Use QuickSort when the average `O(n log n)` log linear time complexity matters more than the worse case `O(n^2)` quadratic time complexity. It also has a good `O(log n)` logarithmic space complexity.
- Use MergeSort when you need a **stable sorting algorithm** with a consistent `O(n log n)` log linear space complexity
- Insertion sort is good for small or nearly sorted lists

| Type           | Best Time  | Average Time | Worst Time | Space    |
| -------------- | ---------- | ------------ | ---------- | -------- |
| Bubble sort    | O(n)       | O(n^2)       | O(n^2)     | O(1)     |
| Selection sort | O(n^2)     | O(n^2)       | O(n^2)     | O(1)     |
| Insertion sort | O(n)       | O(n^2)       | O(n^2)     | O(1)     |
| Merge sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)     |
| Quick sort     | O(n log n) | O(n log n)   | O(n^2)     | O(log n) |

## Elementary sorting

### Bubble sort

**NOTE: Only used for educational purposes**

The bubble sort algorithm traverses the array and compares the first 2 elements. It swaps them if the second element is larger. This continues till the end of the array. The larger values "bubble" their way to the top of the array. After the first traversal through the array, the process is repeated up to the second last element of the array.

```python
def bubble_sort(items):
    """
    Time - O(n^2): Nested for loop.
    Space - O(1): Only 2 integer variables are created.
    """
    max = len(items) - 1
    for _ in range(max):
        for current in range(max):
            next = current + 1
            if items[current] > items[next]:
                items[current], items[next] = items[next], items[current]
    return items
```

### Selection sort

**NOTE: Only used for educational purposes**

```python
def selection_sort(items):
    """
    Time - O(n^2): Nested for loop.
    Space - O(1): Only 2 integer variables are created.
    """
    size = len(items)
    for outer in range(size):
        min = outer
        for inner in range(outer + 1, size):
            if items[inner] < items[min]:
                min = inner
        items[outer], items[min] = items[min], items[outer]
    return items
```

### Insertion sort

- Is best used when their are few items that are mostly sorted

```python
def insertion_sort(items):
    """
    Time - O(n^2): Nested for loop.
    Space - O(1): 3 variables are created. 
         Caution: `value` could be a large data structure.
    """
    for i in range(1, len(items)):
        current = i
        previous = current - 1
        value = items[current]
        while current > 0 and items[previous] > value:
            items[current] = items[previous]
            previous -= 1
            current -= 1
        items[current] = value
    return items
```

## Divide and conquer sorting

### Merge sort

- Generally good sorting algorithm
- Bad for **internal sorting** due to O(n) space complexity
- Good for **external sorting**
- Breaks a data set into individual pieces and merges them
- Uses **recursion** to operate on the input
- Break the array down to single element arrays and merge them back together while sorting

```python
def merge_sort(items):
    """
    Time - O(n log n): Iterate through the list O(n) then iterate through 
        a tree like structure (log n).
    Space - O(n): A new list is created and items are merged into it.
    """
    if len(items) < 2:
        return

    # Split the array and recursively call merge_sort
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:] 
    merge_sort(left)
    merge_sort(right)

    left_index = right_index = items_index = 0

    # While both arrays have items
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            items[items_index] = left[left_index]
            left_index += 1
        else:
            items[items_index] = right[right_index]
            right_index += 1
        items_index += 1

    # Add left side values if any are remaining
    while left_index < len(left):
        items[items_index] = left[left_index]
        left_index += 1
        items_index += 1

    # Add right side values if any are remaining
    while right_index < len(right):
        items[items_index] = right[right_index]
        right_index += 1
        items_index += 1

    return items
```

### Quick sort

- Generally good sorting algorithm
- Decent for **internal sorting** due to O(log n) space complexity
- Good for **external sorting**
- Very bad worst case scenario O(n^2) if a bad pivot is selected
- Breaks a data set into individual pieces and merges them
- Uses **recursion** to operate on the input
- Generally performs better than merge sort, O(n log n)
- Operates in place on data

1. Pick a random pivot item
1. Make all items less than it stay on it's left and all items greater are moved to it's right

```python
def quick_sort(items):
    """
    Time - O(n log n): Iterate through the list O(n) then iterate through 
        a tree like structure (log n).
        CAUTION: Worst case is O(n^2) if the smallest or the largest item in
            the list is selected as the pivot because then the list is not
            being split in half.
    Space - O(log n): 
    """
    def sorter(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high) 
            sorter(items, low, pivot_index-1)
            sorter(items, pivot_index+1, high)

    def partition(items, low, high):
            i = low - 1
            pivot = items[high]
            for j in range(low , high):
                if items[j] <= pivot: 
                    i += 1 
                    items[i], items[j] = items[j], items[i] 
            items[i+1], items[high] = items[high], items[i+1] 
            return i + 1

    sorter(items, 0, len(items) - 1)
    return items
```

- Is best used when a really good pivot is selected

## Non-comparison sort

- Only works with integers in a small range
- Use the way integers are stored in memory

### Counting sort

- https://brilliant.org/wiki/counting-sort
- https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

### Radix sort

- https://brilliant.org/wiki/radix-sort
- https://www.cs.usfca.edu/~galles/visualization/RadixSort.html

## Determine if a list is sorted

```python
def is_sorted(items):
    """
    Brute force.

    Time - O(n): Iterate over all items.
    Space - O(1): No new variables introduced.
    """
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

def is_sorted(items):
    """
    Brute force using Python comprehension.

    Time - O(n): Iterate over all items.
    Space - O(n): New list created via comprehension.
    """
    return all(items[i] <= items[i+1] for i in range(len(items)-1))

def is_sorted(items):
    """
    Return True if the items are sorted. 

    Time - O(log n): Implemented using binary search.
    Space - O(1): Only 2 integer variables are created.

    >>> is_sorted([6, 20, 8]) 
    False
    >>> is_sorted([6, 8, 19])
    True
    """
    lower = 0
    upper = len(items) - 1
    while lower <= upper:
        if items[lower] > items[upper]:
            return False
        lower += 1
        upper -= 1
    return True
```

```python
def max(items):
    """
    Return the highest value in the items. Implemented using recursion.

    Time - O(n): Iterate over all items.
    Space - O(n): Store max function on the call stack.

    >>> max([6, 20, 8]) 
    20
    """
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

## Sort algorithms per language

### Python

> Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was invented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsets of the data that are already ordered, and uses the subsets to sort the data more efficiently. This is done by merging an identified subset, called a run, with existing runs until certain criteria are fulfilled. Timsort has been Python's standard sorting algorithm since version 2.3. It is now also used to sort arrays in Java SE 7, and on the Android platform.

source: http://en.wikipedia.org/wiki/Timsort

### Ruby

Ruby uses Quicksort. source:
https://www.igvita.com/2009/03/26/ruby-algorithms-sorting-trie-heaps/

## References

- https://www.bigocheatsheet.com
- https://www.toptal.com/developers/sorting-algorithms
- https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
- https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap-objects
- https://www.geeksforgeeks.org/sorting-terminology
- https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important
- https://brilliant.org/wiki/heap-sort
- https://stackoverflow.com/questions/2467751/quicksort-vs-heapsort