import unittest


class Node(object):
    """ An item being added to the LinkedList.
    """

    def __init__(self, data, next=None, prev=None):
        """
        :param data: The info being stored in this new node.
        """
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        next = None if self.next is None else self.next.data
        prev = None if self.prev is None else self.prev.data
        return f"Node: {self.data}, Prev: {prev}, Next: {next}"

    def swap(self, node):
        """
        Swap the positions of 2 nodes.

        :param node: The other node to swap with.
        """
        if node is None:
            return
        if self.next is not None and self.next == node:
            temp_prev = self.prev
            temp_next = node.next
            node.next = self
            node.prev = temp_prev
            node.prev.next = node
            self.prev = node
            self.next = temp_next
        elif self.prev is not None and self.prev == node:
            node.swap(self)


class LinkedList(object):
    """ A list of Nodes linked to their next and/or previous Node. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.head
        self.size = 0

    def __len__(self):
        """ Time - O(1): size is calculated on insert/delete. """
        return self.size

    def __str__(self):
        """ 
        Time - O(n): LinkedList traversal
        """
        current = self.head
        output = ""
        while current:
            output += str(current) + "\n"
            current = current.next
        return output

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        """ 
        Retrieve the next data from the LinkedList.

        :return: any or None
        """
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    # Create

    def prepend(self, data):
        """ 
        Add a Node to the beginning of the LinkedList.

        Time - O(1): Because the head is at a known location in memory.

        :param data: The info being stored in this new node.
        :return: bool True if successful.
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
        return True

    def append(self, data):
        """ 
        Add a Node to the end of the LinkedList.

        Time - O(1): Because the tail is at a known location in memory.
        NOTE: if there was no tail, Time - O(n): Because of traversal.

        :param data: The info being stored in this new node.
        :return: bool True if successful.
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
        return True

    def insert(self, position, data):
        """ 
        Insert data at a specific position in the LinkedList.

        Time - O(n): LinkedList traversal.

        :param position: The position the data will be stored in.
        :param data: The info being stored in this new node.
        :return: bool True if successful.
        """
        if position <= 1:
            return self.prepend(data)
        if position > len(self):
            return False
        current = self.find_at(position)
        if current is not None:
            new_node = Node(data, next=current, prev=current.prev)
            new_node.prev.next = new_node
            current.prev = new_node
            self.size += 1
            return True
        return False

    # Find

    # TODO: `find` should return a bool and `_find_node_by` should return a Node or None
    # TODO: `find_at` should return the data and `_find_node_at` should return a Node or None

    def find(self, data):
        """ 
        Find a Node in the LinkedList.

        Time - O(n): LinkedList traversal.

        :param data: The info being retrieved.
        :return: Node object or None
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_at(self, position):
        """ 
        Find a Node in the LinkedList.

        Time - O(n): LinkedList traversal.

        :param position: The position the data will be stored in.
        :return: Node object or None
        """
        if 1 > position > len(self):
            return None
        i = 1
        current = self.head
        while current:
            if i == position:
                return current
            current = current.next
            i += 1
        return None

    # Remove

    def remove(self, data):
        """ Remove a Node from the LinkedList.
        Time - O(n)

        :param data: The info being removed.
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

    def remove_at(self, position):
        """ 
        Remove a Node from the LinkedList.

        Time - O(n)

        :param position: The position the data will be removed.
        """
        unwanted = self.find_at(position)
        if unwanted is None:
            return False
        if unwanted.next is not None:
            unwanted.next.prev = unwanted.prev if unwanted.prev is not None else None
        if unwanted.prev is not None:
            unwanted.prev.next = unwanted.next if unwanted.next is not None else None
        self.size -= 1

    # Additional

    def reverse(self):
        """
        WARNING: This reverses the LinkedList in place. Use with caution.

        Time - O(n): LinkedList traversal.
        """
        current = self.tail
        self.head, self.tail = self.tail, self.head
        while current:
            current.swap(current.prev)
            current = current.prev


class TestNode(unittest.TestCase):
    """ Test the behavior of the Node class. """

    def test_init(self):
        node = Node(2, prev=Node(1), next=Node(3))
        self.assertEqual("Node: 2, Prev: 1, Next: 3", str(node))

    def test_swap(self):
        node = Node(3, prev=Node(1), next=Node(2))
        self.assertEqual("Node: 3, Prev: 1, Next: 2", str(node))

        node.swap(node.next)
        self.assertEqual("Node: 3, Prev: 2, Next: None", str(node))

        node.swap(node.prev)
        self.assertEqual("Node: 3, Prev: 1, Next: 2", str(node))


class TestLinkedList(unittest.TestCase):
    """ Test the behavior of the LinkedList class. """

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

    def test_insert(self):
        self.list.append('a')
        self.list.append('c')
        node = self.list.find_at(2)
        self.assertEqual("Node: c, Prev: a, Next: None", str(node))

        self.list.insert(2, 'b')
        node = self.list.find_at(2)
        self.assertEqual("Node: b, Prev: a, Next: c", str(node))

    def test_find(self):
        self.list.append(2)
        self.assertEqual("Node: 2, Prev: None, Next: None",
                         str(self.list.find(2)))
        self.assertEqual(None, self.list.find(22))

    def test_remove(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

        # Remove invalid node.
        self.list.remove(7)
        self.assertEqual("Node: 2, Prev: 1, Next: 3",
                         str(self.list.find(2)))
        self.assertEqual(3, len(self.list))

        # Remove valid node.
        self.list.remove(2)
        self.assertEqual(None, self.list.find(2))
        self.assertEqual("Node: 1, Prev: None, Next: 3",
                         str(self.list.head))
        self.assertEqual(2, len(self.list))

    def test_remove_at(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')

        # Remove invalid node.
        self.list.remove_at(7)
        self.assertEqual("Node: b, Prev: a, Next: c",
                         str(self.list.find('b')))
        self.assertEqual(3, len(self.list))

        # Remove valid node.
        self.list.remove_at(2)
        self.assertEqual(None, self.list.find(2))
        self.assertEqual("Node: a, Prev: None, Next: c",
                         str(self.list.head))
        self.assertEqual(2, len(self.list))

    def test_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(3, self.list.head.data)
        self.assertEqual(1, self.list.tail.data)


# Run the tests
if __name__ == "__main__":
    unittest.main()
