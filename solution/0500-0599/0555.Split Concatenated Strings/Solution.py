class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [max(s[::-1], s) for s in strs]
        ans = ''.join(strs)
        for i, s in enumerate(strs):
            t = ''.join(strs[i + 1 :]) + ''.join(strs[:i])
            for j in range(len(s)):
                a = s[j:]
                b = s[:j]
                ans = max(ans, a + t + b)
                ans = max(ans, b[::-1] + t + a[::-1])
        return ans
