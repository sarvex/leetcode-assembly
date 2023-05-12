class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        s = set()
        for word in dict:
            for i in range(len(word)):
                t = f"{word[:i]}*{word[i + 1:]}"
                if t in s:
                    return True
                s.add(t)
        return False
