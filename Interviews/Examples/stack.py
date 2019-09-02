class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        next = None if self.next is None else self.next.data
        return f"Node: {self.data}, Next: {next}"


class Stack(object):
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def __str__(self):
        current = self.top
        output = ""
        while current:
            output += str(current.data)
            if current == self.top:
                output += ' * TOP'
            if current == self.bottom:
                output += ' * BOTTOM'
            output += "\n"
            current = current.next
        return output

    def peek(self):
        return self.top

    def push(self, data):
        node = Node(data, next=self.top)
        if self.bottom is None:
            self.bottom = node
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        unwanted = self.top
        self.top = unwanted.next
        self.size -= 1
        return unwanted

    def is_empty(self):
        return self.size == 0


class ListStack(object):
    def __init__(self):
        self.list = []

    # TODO: Determine how to make this more readable for lists.
    def __str__(self):
        output = ""
        for index, item in enumerate(reversed(self.list)):
            output += str(item)
            if index == 0:
                output += ' * TOP'
            if index == len(self.list)-1:
                output += ' * BOTTOM'
            output += "\n"
        return output

    def peek(self):
        return self.list[-1]

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


def test_stack(stack):
    stack.push('Discord')
    stack.push('Udemy')
    stack.push('Google')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())


def main():
    print('\n........testing stack...........')
    test_stack(Stack())
    print('\n........testing list stack...........')
    test_stack(ListStack())


if __name__ == '__main__':
    main()
    print('done!')
