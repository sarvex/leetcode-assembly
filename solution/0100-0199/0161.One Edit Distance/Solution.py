class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        m, n = len(s), len(t)
        if m - n > 1:
            return False
        return next(
            (
                s[i + 1 :] == t[i + 1 :] if m == n else s[i + 1 :] == t[i:]
                for i, c in enumerate(t)
                if c != s[i]
            ),
            m == n + 1,
        )
