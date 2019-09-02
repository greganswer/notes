# Given 2 arrays, write a function that lets a user known
# (true/false) whether these 2 arrays contain common items.

# Questions:
#   - What is the main goal of this function? Time efficiency.
#   - How large will these arrays get? Infinite.


class HasCommonItems(object):
    """ 
    Each static method is the nth attempt at a solution to determine
    if a pair of arrays has common items. 
    """

    @staticmethod
    def first(items1, items2):
        """ 
        Brute force: Use a nested loop to find common item. 
        Time - O(a * b)

        :param items1: first list of items
        :param items2: second list of items
        """
        for i in items1:
            for j in items2:
                if i == j:
                    return True
        return False

    @staticmethod
    def second(items1, items2):
        """ 
        Create a lookup table with the first list. Loop through the 
        second list and return true if any item is in the lookup table
        return false otherwise.

        Time - O(a + b)
        """
        lookup = {val: True for __, val in enumerate(items1)}
        for item in items2:
            if item in lookup:
                return True
        return False

    @staticmethod
    def third(items1, items2):
        """ 
        This solution builds on the second solution and attempts to 
        handle invalid inputs using try except blocks. 
        """
        try:
            lookup = {val: True for __, val in enumerate(items1)}
        except TypeError as e:
            print(e)
            lookup = [items1]

        try:
            iter(items2)
        except TypeError as e:
            print(e)
            items2 = [items2]

        for item in items2:
            if item in lookup:
                return True

        return False

    @staticmethod
    def fourth(items1, items2):
        """ 
        Just use sets because duplicates don't matter. 
        Exception handling in the second solution can be applied here.
        """
        lookup = set(items1)
        other_set = set(items2)
        return bool(lookup & other_set)


def main():
    """ Test the functions.
    """
    arr1 = ["a", "b", "c", "d"]
    arr2 = ["x", "y", "z"]
    arr3 = ["x", "y", "d"]

    # Valid inputs
    assert HasCommonItems.first(arr1, arr2) == False
    assert HasCommonItems.first(arr1, arr3) == True

    assert HasCommonItems.second(arr1, arr2) == False
    assert HasCommonItems.second(arr1, arr3) == True

    assert HasCommonItems.third(arr1, arr2) == False
    assert HasCommonItems.third(arr1, arr3) == True

    assert HasCommonItems.fourth(arr1, arr2) == False
    assert HasCommonItems.fourth(arr1, arr3) == True

    # Invalid inputs
    assert HasCommonItems.third(arr1, []) == False
    assert HasCommonItems.third([], arr2) == False
    assert HasCommonItems.third([], arr3) == False
    assert HasCommonItems.third([], []) == False
    assert HasCommonItems.third(0, []) == False
    assert HasCommonItems.third([], 0) == False
    assert HasCommonItems.third(arr1, "a") == True

    print("passed!")


if __name__ == "__main__":
    main()
