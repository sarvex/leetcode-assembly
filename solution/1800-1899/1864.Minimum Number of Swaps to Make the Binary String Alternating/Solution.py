class Solution:
    def minSwaps(self, s: str) -> int:
        s0n0 = s0n1 = s1n0 = s1n1 = 0
        for i in range(len(s)):
            if (i & 1) == 0:
                if s[i] == '0':
                    s1n1 += 1
                else:
                    s0n0 += 1
            elif s[i] != '0':
                s1n0 += 1
            else:
                s0n1 += 1
        if s0n0 != s0n1:
            return -1 if s1n0 != s1n1 else s1n0
        return s0n0 if s1n0 != s1n1 else min(s0n0, s1n0)
