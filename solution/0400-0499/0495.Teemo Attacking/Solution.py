class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return duration + sum(min(duration, b - a) for a, b in pairwise(timeSeries))
