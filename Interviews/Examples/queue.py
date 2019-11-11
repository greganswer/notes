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


class TestQueue(unittest.TestCase):
    """ Test the behavior of the Queue class. """

    def setUp(self):
        self.queue = Queue()

    def test_init(self):
        self.assertIsNone(self.queue.peek())
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_add(self):
        self.queue.add(1)
        self.queue.add(2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(len(self.queue), 2)

    def test_remove(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.remove()
        self.assertEqual(self.queue.peek(), 2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(len(self.queue), 1)

    def test_remove_when_queue_empty(self):
        self.queue.remove()
        self.assertIsNone(self.queue.peek())
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)


# Run the tests
if __name__ == "__main__":
    unittest.main()
