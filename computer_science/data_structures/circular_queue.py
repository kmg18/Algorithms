class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None for _ in range(k)]
        self.front = -1
        self.back = 0

        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size >= self.capacity:
            return False
        if self.front == -1:
            self.front += 1
        self.queue[self.back % self.capacity] = value
        self.size += 1
        self.back += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.queue[self.front] = 0
        self.front += 1
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.back = 0
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size == 0:
            return -1
        return self.queue[(self.back - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """

        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity

if __name__ == '__main__':
    obj = MyCircularQueue(10)
    print(obj.enQueue(10))
    print(obj.enQueue(20))
    print(obj.enQueue(30))
    print(obj.deQueue())
    print(obj.Front())
    print(obj.Rear())
    print(obj.isEmpty())
    print(obj.isFull())