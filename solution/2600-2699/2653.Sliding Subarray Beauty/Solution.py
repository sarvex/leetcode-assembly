from sortedcontainers import SortedList


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList(nums[:k])
        ans = [min(sl[x - 1], 0)]
        for i in range(k, len(nums)):
            sl.remove(nums[i - k])
            sl.add(nums[i])
            ans.append(min(sl[x - 1], 0))
        return ans
