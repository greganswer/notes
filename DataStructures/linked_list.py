import unittest

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node: {self.data}'

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """O(1) time complexity: size is calculated on insert/delete and is cached."""
        return self.size

    def __str__(self):
        """O(n) time complexity."""
        current = self.head
        output = ""
        while current:
            output += str(current) + '\n'
            current = current.next
        return output

    # Create

    def prepend(self, data):
        """Add a Node to the beginning of the LinkedList.
        O(1) time complexity.
        """
        new_node = Node(data)
        current = self.head
        if current:
            new_node.next = current
            current.prev = new_node
        if not self.tail:
          self.tail = current if current else new_node

        self.head = new_node
        self.size += 1

    def append(self, data):
        """Add a Node to the end of the LinkedList.
        O(n) time complexity.
        """
        current = self.head
        new_node = Node(data)

        if not current:
            self.prepend(data)
            return

        while current.next:
            current = current.next

        new_node.prev = current
        current.next = new_node
        self.tail = new_node
        self.size += 1

    # Find

    def find(self, data):
        """Find a Node in the LinkedList.
        O(n) time complexity.
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next

        return None

    # Delete

    def remove(self, data):
        """Remove a Node from the LinkedList.
        O(1) time complexity if the node is head. Otherwise O(n).
        """
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