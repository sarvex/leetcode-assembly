class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max = 0
        mask = 0
        for i in range(30, -1, -1):
            current = 1 << i
            mask = mask ^ current
            s = {num & mask for num in nums}
            flag = max | current
            for prefix in s:
                if prefix ^ flag in s:
                    max = flag
                    break
        return max
