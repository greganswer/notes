import unittest


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, data):
        self.top = self.Node(data, self.top)
        self.size += 1

    def pop(self):
        if not self.top:
            return
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return not self.top

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class ListStack(object):
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop() if self.list else None

    def peek(self):
        return self.list[-1] if self.list else None

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
