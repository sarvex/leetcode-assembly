class Solution:
    def firstUniqChar(self, s: str) -> str:
        cnt = Counter(s)
        return next((c for c in s if cnt[c] == 1), " ")
