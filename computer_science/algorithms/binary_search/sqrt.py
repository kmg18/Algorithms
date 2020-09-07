'''

Intuition: The basic idea behind this algorithm is to use binary search to find the sqaure root of a given number
if the square root exists.

The time complexity of the algorithm is O(log(n))
Space complexity is O(1)

'''


class SquareRoot(object):

    def sqrt(self, x):

        low = 1
        high = x

        while low <= high:
            mid = low + (high - low)// 2

            if mid * mid == x:
                return mid

            if mid * mid > x:
                high = mid - 1

            else:
                low = mid + 1

        return -1

    def helper(self, x):
        result = self.sqrt(x)
        if result == -1:
            print('not a square root')
        else:
            print(result)




if __name__ == '__main__':
    obj = SquareRoot()
    obj.helper(9) # 3
    obj.helper(40000)  # 200
    obj.helper(80) # Not a square root
    obj.helper(900) # 30