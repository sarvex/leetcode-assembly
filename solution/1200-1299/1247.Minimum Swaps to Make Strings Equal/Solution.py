class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            xy += a < b
            yx += a > b
        return -1 if (xy + yx) % 2 else xy // 2 + yx // 2 + xy % 2 + yx % 2
