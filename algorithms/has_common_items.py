# Given 2 arrays, write a function that lets a user known
# (true/false) whether these 2 arrays contain common items.


# What is the main goal of this function? Time effeciency.
# How large will these arrays get? Infinite.
def has_common_items(items1, items2):
    """ Returns true if the 2 input arrays have any items in common.

    Time - O(a + b)
    """
    # Brute force:
    # Time - O(a * b)
    # for i in items1:
    #     for j in items2:
    #         if i == j:
    #             return True

    # Second attempt:
    # maxLen = len(items1) if len(items1) > len(items2) else len(items2)

    # Third attempt:
    # Create a lookup table with the first list
    # Loop through the second list and return true if any item is in the lookup table
    # Return false otherwise

    # Fourth attempt:
    # Time - O(a + b)
    # This works well but it does not handle invalid inputs
    # lookup = {val: True for __, val in enumerate(items1)}
    # for item in items2:
    #     if item in lookup:
    #         return True

    # Fifth attempt:
    # Handles invalid input
    try:
        lookup = {val: True for __, val in enumerate(items1)}
    except TypeError:
        lookup = [items1]

    try:
        iter(items2)
    except TypeError:
        items2 = [items2]

    for item in items2:
        if item in lookup:
            return True

    return False


arr1 = ['a', 'b', 'c', 'd']
arr2 = ['x', 'y', 'z']
arr3 = ['x', 'y', 'd']

# Valid inputs
assert has_common_items(arr1, arr2) == False
assert has_common_items(arr1, arr3) == True

# Invalid inputs
assert has_common_items(arr1, []) == False
assert has_common_items([], arr2) == False
assert has_common_items([], arr3) == False
assert has_common_items([], []) == False
assert has_common_items(0, []) == False
assert has_common_items([], 0) == False
assert has_common_items(arr1, 'a') == True

print('passed!')
