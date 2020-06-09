import unittest

class Node():
    def __init__(self, data):
        self.val = data
        self.minimum = None
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.minimum = -float('inf')

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.minimum = node.val

        else:
            if node.val < self.minimum:
                self.minimum = node.val
            node.next = self.head
            self.head = node
            self.length += 1
        self.head.minimum = self.minimum

    def pop(self):
        if self.head is None:
            return ('cannot pop from empty stack')

        data = self.head.val
        self.head = self.head.next
        self.length -= 1
        self.minimum = self.head.minimum
        return data

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.head is None:
            print('empty stack')
            return
        return self.head.val
    def getMinimum(self):
        if self.head is None:
            return 'stack is empty'
        return self.minimum

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