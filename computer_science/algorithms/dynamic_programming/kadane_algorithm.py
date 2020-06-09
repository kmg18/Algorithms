class Solution:
    def maxSubArray(self, nums):

        if len(nums) == 0:
            return 0

        tempSum = 0
        maxSum = float('-inf')
        for ele in nums:
            tempSum = max(tempSum + ele, ele)
            maxSum = max(maxSum, tempSum)
        return maxSum

if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([1, -1, 2, 4, -7, 9, -8])) #9
    print(obj.maxSubArray([1, -1, -6, -8, -10])) #1
