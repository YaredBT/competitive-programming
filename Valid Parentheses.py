class Solution:
    def isValid(self, s: str) -> bool:
        par = {'(':')', '[':']', '{': '}'}
        arr = []
        for i in s:
            if i in par:
                arr.append(i)
            elif len(arr) == 0 or par[arr.pop()] != i:
                return False
        return len(arr) ==0
