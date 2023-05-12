class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        return next((i for i, c in enumerate(s) if cnt[c] == 1), -1)
