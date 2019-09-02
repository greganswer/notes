# Given 2 sorted arrays, merge them together in a single sorted array.


class MergeSortedArrays(object):
    @staticmethod
    def first(left, right):
        """
        Brute Force: Merge the 2 arrays and then sort them.

        Time - O(a + b)
        Space - O(a + b)
        """
        return sorted(left + right)

    @staticmethod
    def fifth(left, right):
        """
        Compare the first item of the list 1 to the first item of list 2.
        Add the smaller one to the new output list and increment the index 
        for the list that had the smaller item. Do this until one of the lists
        is empty. Then add the remaining list the the output list.

        Time - O(a + b): Items from both lists must be traversed.
        Space - O(a + b): A new list is created with items from both lists.
        """
        result = []
        i = j = 0
        left_item = left[i]
        right_item = right[j]
        while left_item is not None and right_item is not None:
            if left_item <= right_item:
                result.append(left_item)
                i += 1
                left_item = left[i] if i < len(left) else None
            else:
                result.append(right_item)
                j += 1
                right_item = right[j] if j < len(right) else None
        result.extend(left[i:] if left[i:] else right[j:])
        return result

    @staticmethod
    def with_error_handling(left, right):
        """
        Handle the following invalid inputs:
            - Return an the other list if either list is empty

        Time - O(a + b)
        Space - O(a + b)
        """
        if len(left) == 0:
            return right
        if len(left) == 0:
            return left
        return MergeSortedArrays.fifth(left, right)


def main():
    """ Run the tests. """
    left = [0, 3, 4, 31]
    right = [4, 6, 30]
    result = [0, 3, 4, 4, 6, 30, 31]

    assert MergeSortedArrays.first(left, right) == result
    assert MergeSortedArrays.fifth(left, right) == result

    # with_error_handling
    assert MergeSortedArrays.with_error_handling([], right) == right
    assert MergeSortedArrays.with_error_handling(left, []) == left


if __name__ == "__main__":
    main()
    print("done!")
