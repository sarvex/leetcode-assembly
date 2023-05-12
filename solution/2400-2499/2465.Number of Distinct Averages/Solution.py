class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return len({nums[i] + nums[n - i - 1] for i in range(n >> 1)})
