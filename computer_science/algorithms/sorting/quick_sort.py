"""
Intuition: The basic idea of quicksort is to find the right location of a element (pivot) and once the location is determined,
then sort the left half of elements and sort the right half of elements. Since the pivot is already sorted, the entire
array is aslo sorted.
QuickSort is not a stable sort.
The core part of quicksort algorithm is determining the pivot element.
For choosing pivot element we have three options :
1. Choose the left most element as pivot
2.Choose the right most element as pivot
3. Choose middle element as pivot
4. Choose a random element as pivot

In this program, we'll use last index as pivot and note that for sorted input array the space and time complexities
of this approach are O(n) and O(n*2) respectively.
"""

class Quicksort(object):
    def quicksort(self, input):
        self.quicksortHelper(input, 0, len(input) - 1)

    def quicksortHelper(self, input, low, high):
        if low < high:
            pivot = self.getPivot(input, low, high)
            self.quicksortHelper(input, low, pivot - 1)
            self.quicksortHelper(input, pivot + 1, high)
    def getPivot(self, input, low, high):
        pivot = input[high]
        pIndex = low
        for i in range(low, high):
            if input[i] <= pivot:
                input[i], input[pIndex] = input[pIndex], input[i]
                pIndex += 1

        input[pIndex], input[high] = input[high], input[pIndex]
        return pIndex

if __name__ == '__main__':
    obj = Quicksort()
    input = [9,8,7,6,5,4,3,2,1]
    obj.quicksort(input)
    print(input) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    input = []
    obj.quicksort(input)
    print(input) #[]

    input = [9, 8, -7, 6, -5, 4, 3, -2, 1]
    obj.quicksort(input)
    print(input) # [-7, -5, -2, 1, 3, 4, 6, 8, 9]