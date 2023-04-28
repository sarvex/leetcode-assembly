class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = defaultdict(int)
        ans = 0
        for s in words:
            x = 1
            for i in range(len(s)):
                t = s[:i] + s[i + 1:]
                x = max(x, d[t] + 1)
            d[s] = x
            ans = max(ans, x)
        return ans
