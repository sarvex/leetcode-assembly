class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i, row in enumerate(nums):
            arr.extend((i + j, j, v) for j, v in enumerate(row))
        arr.sort()
        return [v[2] for v in arr]
