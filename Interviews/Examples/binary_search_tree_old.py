import unittest


class Node(object):
    """ An item being added to the BinarySearchTree.
    """

    def __init__(self, data):
        """
        :param data: The info being stored in this new node.
        """
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Node: {self.data}"

    # Create

    def insert(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)

    # Read

    def get_min(self):
        return self.left_child.get_min() if self.left_child else self.data

    def get_max(self):
        return self.right_child.get_max() if self.right_child else self.data

    def traverse_in_order(self):
        if self.left_child:
            self.left_child.traverse_in_order()

        print(self)

        if self.right_child:
            self.right_child.traverse_in_order()

    # Delete

    def remove(self, data, parent):
        if data < self.data and self.left_child:
            self.left_child.remove(data, self)
            return

        if data > self.data and self.right_child:
            self.right_child.remove(data, self)
            return

        if self.left_child and self.right_child:
            self.data = self.right_child.get_min()
            self.right_child.remove(self.data, self)
        elif parent.left_child == self:
            temp = self.left_child if self.left_child else self.right_child
            parent = self.right_child
        elif parent.right_child == self:
            temp = self.left_child if self.left_child else self.right_child
            parent.right_child = temp


class BinarySearchTree(object):
    def __init__(self, data):
        self.root_node = None

    def __getattr__(self, attr):
        """ Delegate missing methods to the root Node if it exists
        """
        if self.root_node:
            return getattr(self.root_node, attr)

    def insert(self, data):
        if self.root_node:
            self.root_node.insert(data)
        else:
            self.root_node = Node(data)

    def remove(self, data):
        if not self.root_node:
            return

        if self.root_node == data:
            temp = Node(None)
            temp.left_child = self.root_node
            self.root_node.remove(data, temp)
        else:
            self.root_node.remove(data, None)

    # TODO: Check if __getattr__ works then delete the following lines
    #
    # def get_max(self):
    #     if self.root_node:
    #         self.root_node.get_max()

    # def get_min(self):
    #     if self.root_node:
    #         self.root_node.get_min()

    # def traverse_in_order(self):
    #     if self.root_node:
    #         self.root_node.traverse_in_order()
