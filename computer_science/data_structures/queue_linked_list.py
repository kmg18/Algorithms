import unittest

class Node():
    def __init__(self, data):
        self.val = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node


    def pop(self):
        if self.head is None:
            return ('cannot pop from empty queue')

        data = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data.val



    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.head is None:
            print('empty queue')
            return
        return self.head.val

class TestCases(unittest.TestCase):

    def test_case1(self):
        queue = Queue()
        queue.append(10)
        queue.append('mukesh')
        self.assertEqual(queue.pop(), 10, "Output should be 10")

    def test_case2(self):
        queue = Queue()
        queue.append(10)
        queue.append('mukesh')
        queue.pop()
        queue.pop()
        self.assertEqual(queue.pop(), 'cannot pop from empty queue', "Cannot pop from empty queue")

if __name__ == '__main__':
    unittest.main()