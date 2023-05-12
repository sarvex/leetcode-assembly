class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            return 0 if x == 0 else x // 5 + f(x // 5)

        def g(k):
            return bisect_left(range(5 * k), k, key=f)

        return g(k + 1) - g(k)
