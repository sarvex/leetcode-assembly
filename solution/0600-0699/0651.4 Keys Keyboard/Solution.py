class Solution:
    def maxA(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(2, i):
                f[i] = max(f[i], f[j - 2] * (i - j + 1))
        return f[n]
