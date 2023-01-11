class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        count=0
        for num in nums:
            if num in dic:
                count += dic[num]
                dic[num] += 1
            else:
                dic[num] = 1
        return count
