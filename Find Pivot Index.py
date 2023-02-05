class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for index, value in enumerate(nums):
            rightSum -= value
            if leftSum == rightSum:
                return index
            leftSum += value
        return -1 
