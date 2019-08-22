# Given a list of numbers and an expected sum, determine if
# the sum of any 2 numbers in the array equal to the sum input.


class HasPairWithSum(object):
    """ 
    Determine if items has 2 values that are equal to the sum provided.
    """

    @staticmethod
    def first(items, sum):
        """ 
        Brute force: Use a nested loop and determine if the sum of 
        2 values is equal to the input sum.

        Time - O(n^2)
        Space - O(1)
        """
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] + items[j] == sum:
                    return True
        return False

    @staticmethod
    def second(items, sum):
        """ 
        For each item, subtract it from the sum and search the 
        list for that item.

        Time - O(n)
        Space - O(n)
        """
        lookup = {}
        for item in items:
            val = sum - item
            if lookup.get(val):
                return True
            lookup[val] = True
        return False

    @staticmethod
    def third(items, sum):
        """ 
        Assuming the list is already sorted, Subtract the lowest number from the 
        highest number. If the result is greater than the sum, the previous number 
        becomes the highest number. If the result is lower than the sum the next 
        number becomes the lowest number. If the result is equal to the input sum, 
        return True.

        Time - O(log n)
        Space - O(1)
        """
        low_index = 0
        high_index = len(items) - 1
        while low_index < high_index:
            total = items[high_index] + items[low_index]
            if total == sum:
                return True
            if total > sum:
                high_index -= 1
            if total < sum:
                low_index += 1
        return False

    @staticmethod
    def fourth(items, sum):
        """
        Handle the following invalid inputs:
            - None iterable items
            - items length less than 2
            - sum not an integer

        Time - O(log n)
        Space - O(1)
        """
        if not isinstance(sum, int):
            return False
        try:
            assert len(items) > 2
        except (TypeError, AssertionError):
            return False
        return HasPairWithSum.third(items, sum)


def main():
    """ Test the functions. """
    invalid_items = [1, 2, 4, 9]
    valid_items = [1, 2, 4, 4]
    sum = 8

    assert HasPairWithSum.first(invalid_items, sum) == False
    assert HasPairWithSum.first(valid_items, sum) == True

    assert HasPairWithSum.second(invalid_items, sum) == False
    assert HasPairWithSum.second(valid_items, sum) == True

    assert HasPairWithSum.third(invalid_items, sum) == False
    assert HasPairWithSum.third(valid_items, sum) == True

    # Invalid input
    assert HasPairWithSum.fourth(8, sum) == False
    assert HasPairWithSum.fourth([8], sum) == False
    assert HasPairWithSum.fourth(None, sum) == False
    assert HasPairWithSum.fourth(valid_items, "hi") == False
    assert HasPairWithSum.fourth(valid_items, None) == False


if __name__ == "__main__":
    main()
    print("passed!")
