class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {n:i for i, n in enumerate(nums1)}
        arr = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = hash[val]
                arr[index] = cur
            if cur in hash:
                stack.append(cur)

        return arr
