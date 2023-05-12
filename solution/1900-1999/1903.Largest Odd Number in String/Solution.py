class Solution:
    def largestOddNumber(self, num: str) -> str:
        return next(
            (
                num[: i + 1]
                for i in range(len(num) - 1, -1, -1)
                if (int(num[i]) & 1) == 1
            ),
            '',
        )
