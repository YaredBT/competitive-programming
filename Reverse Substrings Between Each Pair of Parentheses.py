class Solution:
    def reverseParentheses(self, s: str) -> str:

        result = []
        i = 0
        while i < len(s):
            if s[i] == ')':
                temp = ""
                while result[-1] != '(':
                    temp += result.pop()
                result.pop()
                for char in temp:
                    result.append(char)
            else:
                result.append(s[i])
            i += 1
        return "".join(result)
