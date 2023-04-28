class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        f = g = 1
        for a, b in pairwise(nums):
            if a < b:
                f = max(f, g + 1)
            if a > b:
                g = max(g, f + 1)
        return max(f, g)
