class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        ans, x = 0, 1
        while x**2 <= g:
            if g % x == 0:
                ans += 1
                ans += x**2 < g
            x += 1
        return ans
