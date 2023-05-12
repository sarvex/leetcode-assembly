class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i, n = 0, len(s)
        t = []
        while i < n:
            cnt = 1
            while i + 1 < n and s[i + 1] == s[i]:
                cnt += 1
                i += 1
            t.append(cnt)
            i += 1
        return sum(min(t[i - 1], t[i]) for i in range(1, len(t)))
