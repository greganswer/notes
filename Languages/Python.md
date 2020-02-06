# Python

  - [General](#general)
  - [Comparison](#comparison)
    - [Is vs. equality operator](#is-vs-equality-operator)
    - [Type function vs. isinstance function](#type-function-vs-isinstance-function)
  - [Data structures](#data-structures)
    - [Truthy and falsey values](#truthy-and-falsey-values)
    - [Strings](#strings)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Dictionaries](#dictionaries)
    - [Sets](#sets)
    - [Classes](#classes)
    - [Modules](#modules)
    - [Comprehensions](#comprehensions)
  - [Control flow](#control-flow)
    - [Exceptions](#exceptions)
  - [Functions](#functions)
    - [Sorting](#sorting)
  - [Command line](#command-line)
    - [Console input and output](#console-input-and-output)
    - [App boilerplate](#app-boilerplate)
  - [Additional reading](#additional-reading)
  - [References](#references)

## General

Python, named after the British comedy group Monty Python, is an interpreted, interactive, object-oriented programming language. Python is:

**Strongly typed**. It enforces data types so you can’t concatenate a string and a integer, for example.
**Dynamically, implicitly typed**. So, you don’t have to explicitly declare variable data types. Data types are enforced at runtime.
**Case sensitive**. For example, token and TOKEN are two different variables.
**Object-oriented**. Everything is an object.

```python
import keyword

print(keyword.kwlist)
[
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'async',
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield'
    ]
```

## Comparison

Seeing whether a value is in a range

```python
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False

# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False
```

Don't use the equality `==` symbol to compare objects to `None` use `is` instead.
This checks for equality of object identity.

```python
"etc" is None  # => False
None is None   # => True
```

### Is vs. equality operator

`is` checks if two variables refer to the same object, but `==` checks if the
objects pointed to have the same values.

```python
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal
```

### Type function vs. isinstance function

`isinstance()` checks for subclasses, `type()` does not.

```python
class Vehicle(object):
    pass

class Truck(Vehicle):
    pass

isinstance(Vehicle(), Vehicle)  # returns True
type(Vehicle()) == Vehicle      # returns True
isinstance(Truck(), Vehicle)    # returns True
type(Truck()) == Vehicle        # returns False, and this probably won't be what you want.
```
## Data structures

### Truthy and falsey values

The following values evaluate to false:

```python
None
False
0
"" # Empty string
[] # Empty list
{} # Empty dict
() # Empty tuple
set() # Empty set
range(0) # Empty range
```

### Strings

You can repeat the formatting arguments to save some typing.
```python
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"
```

You can also format using f-strings or formatted string literals (in Python 3.6+)

```python
# You can basically put any Python statement inside the braces and it will be output in the string.
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."
```

### Lists

List are Python's implementation of arrays.

```python
# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # => [2, 4]
# Omit the beginning and return the list
li[2:]    # => [4, 3]
# Omit the end and return the list
li[:3]    # => [1, 2, 4]
# Select every second entry
li[::2]   # =>[1, 4]
# Return a reversed copy of the list
li[::-1]  # => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 6

four_nones = [None] * 4 # => [None, None, None, None]
```

### Tuples

```python
Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True
```

### Dictionaries

```python
# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+


# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
```

### Sets

```python
empty_set = set()
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set              # => {3, 4, 5}
filled_set.intersection(other_set)  # => {3, 4, 5}

# Check if two sets have no value in common (an intersection that is empty)
filled_set.isdisjoint(other_set)  # => False
filled_set.isdisjoint({7, 8})  # => True

# Do set union with |
filled_set | other_set      # => {1, 2, 3, 4, 5, 6}
filled_set.union(other_set) # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}            # => {1, 4}
{1, 2, 3, 4}.difference({2, 3, 5})  # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}                      # => {1, 4, 5}
{1, 2, 3, 4}.symmetric_difference({2, 3, 5})  # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3}        # => True
{1, 2}.issubset({1, 2, 3}) # => True

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

# Set comprehension
{skill for skill in ['GIT', 'PYTHON', 'SQL'] if skill not in {'GIT', 'PYTHON', 'JAVA'}} # => {'SQL'}

# Create a frozen set
immutableSet = frozenset()
```

### Classes

```python
class Creature(object):
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        self.age = 0


class Human(Creature):
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    def __init__(self, name):
        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # A class method is shared among all instances. They are called with the
    # calling class as the first argument. We generally use class method to
    # create factory methods. Factory methods return class object
    # (similar to a constructor) for different use cases.
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference. It's a
    # way of putting a function into a class (because it logically belongs there),
    # while indicating that it does not require access to the class.
    # We generally use static methods to create utility functions.
    @staticmethod
    def grunt():
        return "*grunt*"


h = Human()
print(h.get_species()) # => H. sapiens

Human.species = "H. neanderthalensis"
print(h.get_species()) # => H. neanderthalensis
print(Human.grunt())   # => *grunt*
```

For more info about the difference between `@staticmethod` and `@classmethod`
reference https://stackoverflow.com/a/1669524.

### Modules

```python
import math
```

```python
def main():
    print("Doing some work...")

# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    main()
```

If you have a Python script named `math.py` in the same folder as your current
script, the file math.py will be loaded instead of the built-in Python module.
This happens because the local folder has priority over Python's built-in libraries.

### Comprehensions

Comprehensions provide a concise way to create lists or dictionaries. It consists of
brackets containing an expression followed by a for clause, then zero or more for or
if clauses. The expressions can be anything, meaning you can put in all kinds of
objects in lists.

```python
[ expression for item in list if conditional ]

# This is equivalent to:
for item in list:
    if conditional:
        expression
```

Examples

```python
[i for i in range(3)]          # => [0, 1, 2, 3]
[i*3 for item in range(3)]     # => [0, 3, 6, 9]
{x: f'A{x}' for x in range(3)} # => {0: 'A0', 1: 'A1', 2: 'A2'}

numbers = [x for x in "Hello 12345 World" if x.isdigit()] # => ['1', '2', '3', '4', '5']

listOfWords = ["this","is","a","list","of","words"]
items = [word[0] for word in listOfWords] # => ['t', 'i', 'a', 'l', 'o', 'w']
```

## Control flow

**Ternary operator**

```python
is_selected = True
output = "Yes" if is_selected else "No"
```

```python
# iterate over lists
for animal in ["dog", "cat", "mouse"]:
    print(f"{animal} is a mammal")

# iterate over lists with index
items = ["dog", "cat", "mouse"]
for i, value in enumerate(items):
    print(i, value)

# iterate over sequential numbers
# => 0, 1, 2, 3
for i in range(4):
    print(i)

# Range starting from 4, going to 8, step by 2
# => 4, 6
for i in range(4, 8, 2):
    print(i)
```

### Exceptions

```python
Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)
```

## Functions

```python
# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sorting

```python
# Sort by value in ascending order
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}

# The `items` method returns each key/value pair as a tuple.
for k, v in sorted(incomes.items(), key=lambda item : item[1]):
    print(f'{k} -> {v}')
```

## Command line

### Console input and output

By default the print function also prints out a newline at the end. Use the
optional argument end to change the end string.

```python
print("Hello, World", end="!")  # => Hello, World!
```

Simple way to get input data from console

```python
input_string_var = input("Enter some data: ") # Returns the data as a string
```

Note: In earlier versions of Python, input() method was named as raw_input()

### App boilerplate

```python
import click
import sys


# Ref: https://youtube.com/watch?v=ubXXmQzzNGo
@click.command()
@click.argument('infile', type=click.File('r'), default='-')  # Optional: From example
@click.argument('outfile', type=click.File('w'), default='-') # Optional: From example
@click.option('--log-file', '-l', type=click.File('w'), default=sys.stderr)
@click.option('--verbose', '-v', is_flag=True)
def cli(infile, outfile, log_file, verbose):
    if verbose:
        click.echo(f'Infile: {infile}', file=log_file)
    click.echo('logging some data...', file=log_file)
    click.secho('printing with colors', file=outfile, fg='green')
    if verbose:
        click.echo('Done!', file=log_file)
```

## Additional reading

1. https://nicedoc.io/aneagoie/ztm-python-cheat-sheet?theme=light
1. https://www.toptal.com/python#hiring-guide
1. https://realpython.com/introduction-to-python-generators/
1. https://realpython.com/python-memory-management/
1. https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python
1. https://docs.python-guide.org/writing/tests
1. https://docs.python-guide.org/writing/structure
1. https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch04.html
1. https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python
1. https://rszalski.github.io/magicmethods
1. https://wiki.python.org/moin/TimeComplexity
1. https://realpython.com/python-range/
1. https://realpython.com/introduction-to-python-generators/
1. https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

## References

Mosts of the examples in this file come directly from one of the following links:

- https://realpython.com/python-testing
- https://learnxinyminutes.com/docs/python3
- https://realpython.com/python-first-steps
- https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
- https://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
- https://docs.python-guide.org/
- https://www.datacamp.com/community/tutorials/sets-in-python
- https://realpython.com/iterate-through-dictionary-python
- https://www.toptal.com/python/an-introduction-to-mocking-in-python
- https://www.toptal.com/python/why-are-there-so-many-pythons
- https://realpython.com/python-virtual-environments-a-primer
- https://realpython.com/python-application-layouts/
