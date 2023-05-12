class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        letters = set(brokenLetters)
        res = 0
        for word in text.split():
            find = any(letter in word for letter in letters)
            if not find:
                res += 1
        return res
