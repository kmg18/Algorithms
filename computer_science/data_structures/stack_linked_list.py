import unittest

class Node():
    def __init__(self, data):
        self.val = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            return ('cannot pop from empty stack')

        data = self.head.val
        self.head = self.head.next
        return data

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.head is None:
            print('empty stack')
            return
        return self.head.val

class TestCases(unittest.TestCase):

    def test_case1(self):
        stack = Stack()
        stack.append(10)
        stack.append('mukesh')
        self.assertEqual(stack.pop(), 'mukesh', "Output should be mukesh")

    def test_case2(self):
        stack = Stack()
        stack.append(10)
        stack.append('mukesh')
        stack.pop()
        stack.pop()
        self.assertEqual(stack.pop(), 'cannot pop from empty stack', "Cannot pop from empty stack")

if __name__ == '__main__':
    unittest.main()