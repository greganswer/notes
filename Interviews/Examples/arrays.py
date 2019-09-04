def one_away_test():
    def one_away(left, right):
        """
        Check if 2 strings are 1 edit away from being the same.

        There are three types of edits that can be performed on strings: 
        insert a character, remove a character, or replace a character. 
        Given two strings, write a function to check if they are one edit 
        (or zero edits) away.

        Time - O(n): Length of shortest string
        Space - O(1)

        Reference: 
            Cracking the Coding Interview, 6th Edition, Chapter 1, question 1.5
        """
        if abs(len(left) - len(right)) > 1:
            return False
        i = diff_count = 0
        size = min(len(left), len(right))
        while i < size:
            if left[i] != right[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
                left_next = left[i+1] if i < len(left) else ""
                right_next = right[i+1] if i < len(right) else ""
                if left_next == right_next or left[i] == right_next or right[i] == left_next:
                    i += 1
                else:
                    return False
            i += 1
        return True

    # Testing
    assert one_away('pale', 'ple')
    assert one_away('pales', 'pale')
    assert one_away('pale', 'bale')
    assert one_away('pale', 'bake') == False
    assert one_away('pale', 'park') == False
    assert one_away('pale', 'pa') == False


one_away_test()
