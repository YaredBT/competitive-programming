class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total = 0
        piles.sort()
        for i in range(len(piles)//3):
            total += piles[len(piles) - 2*(i+1)] 
        return total
