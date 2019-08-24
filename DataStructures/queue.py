class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = None
        self.last = None
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        new_node = Node(x)
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        self.size += 1
        if self.first is None:
            self.first = new_node

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.first is None or self.last is None:
            return 0
        unwanted_node = self.first
        self.first = unwanted_node.next
        self.size -= 1
        return unwanted_node.data

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.first.data if self.first is not None else 0

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0
