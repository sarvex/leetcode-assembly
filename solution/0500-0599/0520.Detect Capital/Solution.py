class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(1 for c in word if c.isupper())
        return cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())
