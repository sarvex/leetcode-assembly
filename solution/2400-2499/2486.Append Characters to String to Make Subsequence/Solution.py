class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        for i, j in enumerate(range(n)):
            while i < m and s[i] != t[j]:
                i += 1
            if i == m:
                return n - j
        return 0
