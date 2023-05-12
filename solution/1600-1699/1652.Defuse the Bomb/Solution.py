class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        s = list(accumulate(code + code, initial=0))
        for i in range(n):
            ans[i] = s[i + k + 1] - s[i + 1] if k > 0 else s[i + n] - s[i + k + n]
        return ans
