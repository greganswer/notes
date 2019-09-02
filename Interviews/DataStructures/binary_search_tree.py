class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, data):
        self.root = None

    def insert(self,data):
        """
        Insert data into the tree.
        """
        new_node = Node(data)
        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
        self.root = new_node

    def lookup(self, data):
        """
        Find data in the tree.
        """
        current = self.root
        while current:
            if current.data == data:
                return current
            current = current.left if data < current.data else current.right

    def remove(self, data):
        """
        Remove data from the tree.
        """
        unwanted = parent = self.root
        while unwanted:
            if unwanted.data == data:
                break
            parent = unwanted
            unwanted = unwanted.left if data < unwanted.left else unwanted.right
        if unwanted is None:
            return
        if unwanted.right is None:
            parent.right = unwanted.left
            return
        if unwanted.right.left is None:
            unwanted.right.left = unwanted.left
            parent.right = unwanted
            return
        parent_of_lowest = lowest = unwanted.right.left
        while lowest:
            if lowest.left is None:
                parent.right = lowest
                parent.right.right = parent_of_lowest
                parent_of_lowest.left = None
                return
            parent_of_lowest = lowest
            lowest = lowest.left

    def remove(self, data):
        pass

