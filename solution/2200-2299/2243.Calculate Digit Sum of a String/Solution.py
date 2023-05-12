class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            t = []
            n = len(s)
            for i in range(0, n, k):
                x = sum(int(s[j]) for j in range(i, min(i + k, n)))
                t.append(str(x))
            s = "".join(t)
        return s
