class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        hashmap = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            hashmap[num] += 1
            
            while hashmap[0] > k:
                hashmap[nums[left]] -= 1
                left += 1
                
            window_size = right - left + 1
            result = max(result, window_size)
            
        return result
