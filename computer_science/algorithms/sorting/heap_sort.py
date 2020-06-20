"""
Intuition: The basic idea in using heaps to sort a list of values is: If we are able to acquire maximum/minimum element
and add that element to the end of list and repeat these operations until all the elements are finished, we end up
having a sorted array.

The Time complexity of a basic heapify operation is O(n)
The Time complexity of heapifyUp and heapigyDown operations are O(log(n))
The overall time complexity of this heapsort algorithm is O(n*log(n))
This heapsort performs sorting in place and has O(1) space complexity

The main reason why quicksort is prefered over heapsort even though both of these operations have equal asymptotic
run time complexity is, in real time quicksort performs swap operations only when required. Whereas heapsort/mergesort
algorithm perform swap operations on all the input elements.
Hence, the actual time to sort using quicksort is way less when compared with heapsort

"""



import heapq
class Heapsort(object):
    def heapsort(self, input):
        heapq.heapify(input)
        self.length = len(input)

        while self.length >= 2:
            element = input[0]
            input[0], input[self.length-1] = input[self.length-1], input[0]
            self.length -= 1
            self.heapifyDown(input)


    def parentIndex(self, index):
         (index - 2) // 2

    def leftChildIndex(self, index):
        check = 2 * index + 1
        if check >= self.length:
            return -1
        return check

    def rightChildIndex(self, index):
        check = 2 * index + 2
        if check >= self.length:
            return -1
        return check

    def heapifyUp(self, input, index):
        while index != 0:
            parentIndex = self.parentIndex(index)
            if input[parentIndex] > input[index]:
                input[parentIndex], input[index] = input[index], input[parentIndex]
                index = parentIndex
            else:
                break

    def heapifyDown(self, input):
        index = 0
        while True:
            leftChildIndex = self.leftChildIndex(index)
            rightChildIndex = self.rightChildIndex(index)

            if leftChildIndex == -1 and rightChildIndex == -1:
                break

            if rightChildIndex == -1:
                if input[leftChildIndex] < input[index]:
                    input[leftChildIndex], input[index] = input[index], input[leftChildIndex]
                    index = leftChildIndex
                    continue
                else:
                    break

            minIndex = -1
            if input[leftChildIndex] < input[rightChildIndex]:
                minIndex = leftChildIndex
            else:
                minIndex = rightChildIndex

            if input[minIndex] < input[index]:
                input[minIndex], input[index] = input[index], input[minIndex]
                index = minIndex
            else:
                break

if __name__ == '__main__':
    obj = Heapsort()
    input = [5,7,9,1,3,2,4,6,8]
    obj.heapsort(input)
    print(input) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

    input = [5]
    obj.heapsort(input)
    print(input) # [5]

    input = [-1, 10, 15, -8, 6, 25, 15]
    obj.heapsort(input)
    print(input) # [25, 15, 15, 10, 6, -1, -8]
