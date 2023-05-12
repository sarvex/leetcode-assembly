class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        while left < right:
            mid = (left + right) >> 1
            cnt = sum(min(mid // i, n) for i in range(1, m + 1))
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return left
