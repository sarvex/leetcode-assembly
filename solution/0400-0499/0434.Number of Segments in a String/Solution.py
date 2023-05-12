class Solution:
    def countSegments(self, s: str) -> int:
        return sum(
            1 for i, c in enumerate(s) if c != ' ' and (i == 0 or s[i - 1] == ' ')
        )
