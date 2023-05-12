class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def gen(self, word):
        return [f'{word[:i]}*{word[i + 1:]}' for i in range(len(word))]

    def buildDict(self, dictionary: List[str]) -> None:
        self.s = set(dictionary)
        self.cnt = Counter(p for word in dictionary for p in self.gen(word))

    def search(self, searchWord: str) -> bool:
        return any(
            self.cnt[p] > 1 or (self.cnt[p] == 1 and searchWord not in self.s)
            for p in self.gen(searchWord)
        )


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
