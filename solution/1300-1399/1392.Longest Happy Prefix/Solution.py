class Solution:
    def longestPrefix(self, s: str) -> str:
        return next((s[i:] for i in range(1, len(s)) if s[:-i] == s[i:]), '')
