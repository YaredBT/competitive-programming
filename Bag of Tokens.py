class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        l = 0
        r = n
        score = 0
        ans = 0
        tokens.sort()
        
        while l < r:
            if power >= tokens[l]:
                power -= tokens[l]
                score+=1
                l+=1
                ans = max(ans, score)
            elif score >= 1 and r> l + 1:
                r-=1
                power += tokens[r]
                score-=1
            else: 
                return ans
            
        return ans
