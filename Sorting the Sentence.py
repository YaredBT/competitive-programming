class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        newArr = [""] * len(arr)
        for i in range(len(arr)):
            for word in arr:
                if int(word[-1]) == i+1:
                    newArr[i] = word[:-1]

        return " ".join(newArr)
