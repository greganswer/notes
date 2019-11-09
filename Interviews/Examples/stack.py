import unittest


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1

    def peek(self):
        if self.top:
            return self.top.data

    def is_empty(self):
        return not self.top

    def pop(self):
        if not self.top:
            return
        removed = self.top
        self.top = removed.next
        self.size -= 1
        return removed.data


class ListStack(object):
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def peek(self):
        if self.list:
            return self.list[-1]

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.list:
            return
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


class TestStack(unittest.TestCase):
    """ Test the behavior of the Stack and ListStack classes. """

    def setUp(self):
        self.stacks = [Stack(), ListStack()]

    def test_init(self):
        for stack in self.stacks:
            self.assertIsNone(stack.peek())
            self.assertTrue(stack.is_empty())
            self.assertEqual(len(stack), 0)

    def test_push(self):
        for stack in self.stacks:
            stack.push(1)
            stack.push(2)
            self.assertEqual(stack.peek(), 2)
            self.assertFalse(stack.is_empty())
            self.assertEqual(len(stack), 2)

    def test_pop(self):
        for stack in self.stacks:
            stack.push(1)
            stack.push(2)
            stack.pop()
            self.assertEqual(stack.peek(), 1)
            self.assertFalse(stack.is_empty())
            self.assertEqual(len(stack), 1)

    def test_pop_when_stack_empty(self):
        for stack in self.stacks:
            stack.pop()
            self.assertIsNone(stack.peek())
            self.assertTrue(stack.is_empty())
            self.assertEqual(len(stack), 0)


# Run the tests
if __name__ == "__main__":
    unittest.main()
