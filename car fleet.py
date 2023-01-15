class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets = cur_time = 0    
        for pos, speed in sorted(pairs, reverse=True):
            destination_time = (target - pos)/speed
            if cur_time < destination_time:
                fleets += 1
                cur_time = destination_time

        return fleets
