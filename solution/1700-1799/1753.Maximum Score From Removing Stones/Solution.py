class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        return a + b if a + b < c else (a + b + c) >> 1
