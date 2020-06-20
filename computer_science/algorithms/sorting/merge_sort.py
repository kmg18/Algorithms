"""
The time and space complexities of merge sort are O(nlog(n)) and O(n) respectively.
Due to heavy soace usage, merge sort is not implementing in default sorting algorithms in various programming
languages. Algorithms like : QuickSort() deliever similar performance with O(log((n)) space requirement. Hence,
Quick sort is prefered over merge sort.
Merge sort is a stable sort.

"""


class Mergesort(object):
    def mergesort(self, input):
        self.mergesortHelper(input, 0, len(input) - 1)

    def mergesortHelper(self, input, low, high):

        if low < high:
            mid = (low + high) // 2
            self.mergesortHelper(input, low, mid)
            self.mergesortHelper(input, mid+1, high)
            self.mergeOperation(input, low, high)

    def mergeOperation(self, input, low, high):
        temp = [0 for _ in range(high - low +1)]
        i, mid = low, (low+ high)//2
        j = mid + 1
        k = 0

        while i <= mid and j <= high:
            if input[i] < input[j]:
                temp[k] = input[i]
                i += 1
            else:
                temp[k] = input[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = input[i]
            i += 1
            k += 1
        while j <= high:
            temp[k] = input[j]
            j += 1
            k += 1

        #copy operation of temp into input array
        for i in range(low, high+1):
            input[i] = temp[i - low]

if __name__ == '__main__':
    obj = Mergesort()
    input1 = [8, 9, 1, 5, 4 ,3, 2, 7, 6, 1,2, 3, 4, 5, 6, 7, 8, 9]
    input2 = [1,1,1,1,1,1,1,1,1,1]
    obj.mergesort(input1)
    print(input1) # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    print(input2) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
