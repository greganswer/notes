import unittest

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    # O(1) time complexity: size is calculated on insert/delete and is cached.
    def __len__(self):
        return self.size

    # O(n) time complexity.
    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current) + '\n'
            current = current.next
        return output

# Create
    # O(1) time complexity.
    def prepend(self, data):
        """Add a Node to the beginning of the LinkedList"""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    # O(n) time complexity.
    def append(self, data):
        """Add a Node to the end of the LinkedList"""
        node = Node(data)
        current = self.head

        if not current:
            self.prepend(data)
            return

        while current.next is not None:
            current = current.next

        node.prev = current
        current.next = node
        self.size += 1

# Find
    # O(n) time complexity.
    def find(self, data):
        """Find a Node in the LinkedList"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next

        return None

# Delete
    # O(1) time complexity if the node is head. Otherwise O(n).
    def remove(self, data):
        """Remove a Node from the LinkedList"""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1

            previous = current
            current = current.next
        
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node: {self.data}'

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_init(self):
        self.assertEqual(0, len(self.list))

    def test_append_and_prepend(self):
        self.list.append(2)
        self.assertEqual(2, self.list.head.data)
        self.assertEqual(2, self.list.tail.data)

        self.list.append(3)
        self.assertEqual(2, self.list.head.data)
        self.assertEqual(3, self.list.tail.data)

        self.list.prepend(1)
        self.assertEqual(1, self.list.head.data)
        self.assertEqual(3, self.list.tail.data)
        self.assertEqual(3, len(self.list))

    def test_find(self):
        self.list.append(2)
        self.assertEqual('Node: 2', str(self.list.find(2)))
        self.assertEqual(None, self.list.find(22))

    def test_remove(self):
        self.list.append(2)

        # Remove invalid node.
        self.list.remove(7)
        self.assertEqual('Node: 2', str(self.list.find(2)))
        self.assertEqual(1, len(self.list))

        # Remove valid node.
        self.list.remove(2)
        self.assertEqual(None, self.list.find(2))
        self.assertEqual(0, len(self.list))


if __name__ == '__main__':
    unittest.main()
