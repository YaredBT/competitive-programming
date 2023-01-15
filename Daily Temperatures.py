class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        arr = []
        for day, temp in enumerate(temperatures):
            while arr and temperatures[arr[-1]] < temp:
                day_before = arr.pop()
                output[day_before] = day - day_before
            arr.append(day)
        return output
