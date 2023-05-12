class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        return next((i for i, v in enumerate(nums) if i % 10 == v), -1)
