class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return words.count(s[: len(word)])
