class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        cnt = [[0] * 26]
        for i, c in enumerate(s, 1):
            j = ord(c) - ord('a')
            t = cnt[-1][:]
            t[j] += 1
            cnt.append(t)
        return [
            sum((b - a) & 1 for a, b in zip(cnt[right + 1], cnt[left])) // 2 <= k
            for left, right, k in queries
        ]
