class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        while i**2 < n:
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
            i += 1
        if i**2 != n:
            i -= 1
        while i:
            if (n % (n // i)) == 0:
                k -= 1
                if k == 0:
                    return n // i
            i -= 1
        return -1
