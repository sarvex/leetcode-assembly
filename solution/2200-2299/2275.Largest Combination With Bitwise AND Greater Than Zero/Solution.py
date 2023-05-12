class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            t = sum((x >> i) & 1 for x in candidates)
            ans = max(ans, t)
        return ans
