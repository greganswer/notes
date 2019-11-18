import unittest


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, data):
        new_node = self.Node(data)
        if self.last:
            self.last.next = new_node
        if not self.first:
            self.first = new_node
        self.last = new_node
        self.size += 1

    def peek(self):
        return self.first.data if self.first else None

    def is_empty(self):
        return not self.first

    def remove(self):
        if not self.first:
            return
        data = self.first.data
        self.first = self.first.next
        if not self.first.next:
            self.last = self.first
        self.size -= 1
        return data

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next


class QueueOfStacks:
    def __init__(self):
        self.push_stack = Stack()  # TODO: Implement
        self.pop_stack = Stack()

    def __len__(self):
        return len(self.push_stack) + len(self.pop_stack)

    # 0(1) constant time
    # O(1) constant space
    def add(self, data):
        self.push_stack.push(data)

    def peek(self):
        self.move_to_pop_stack_if_empty()
        return None if self.pop_stack.is_empty() else self.pop_stack.peek()

    def is_empty(self):
        return not self.peek()

    # O(1) constant time (amortized)
    # O(n) linear space
    def remove(self):
        self.move_to_pop_stack_if_empty()
        return self.pop_stack.pop()

    # O(n) linear time
    # O(1) constant space
    def move_to_pop_stack_if_empty(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                data = self.push_stack.pop()
                self.pop_stack.push(data)


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


class TestQueue(unittest.TestCase):
    """ Test the behavior of the Queue class. """

    def setUp(self):
        self.queues = [Queue(), QueueOfStacks()]

    def test_init(self):
        for queue in self.queues:
            self.assertIsNone(queue.peek())
            self.assertTrue(queue.is_empty())
            self.assertEqual(len(queue), 0)

    def test_add(self):
        for queue in self.queues:
            queue.add(1)
            queue.add(2)
            self.assertEqual(queue.peek(), 1)
            self.assertFalse(queue.is_empty())
            self.assertEqual(len(queue), 2)

    def test_remove(self):
        for queue in self.queues:
            queue.add(1)
            queue.add(2)
            queue.remove()
            self.assertEqual(queue.peek(), 2)
            self.assertFalse(queue.is_empty())
            self.assertEqual(len(queue), 1)

    def test_remove_when_queue_empty(self):
        for queue in self.queues:
            queue.remove()
            self.assertIsNone(queue.peek())
            self.assertTrue(queue.is_empty())
            self.assertEqual(len(queue), 0)


# Run the tests
if __name__ == "__main__":
    unittest.main()
