class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefixSum = [1 if n & 1 else 0 for n in nums]
        for i in range(len(nums)):
            prefixSum[i] += prefixSum[i-1] if i-1 >= 0 else 0
        result = 0
        hashmap = {0: 1}
        for num in prefixSum:
            if num - k in hashmap:
                result += hashmap[num-k]
            hashmap[num] = hashmap.get(num, 0) + 1
        return result
