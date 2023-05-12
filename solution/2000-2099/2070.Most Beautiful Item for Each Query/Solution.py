class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = [p for p, _ in items]
        mx = [items[0][1]]
        mx.extend(max(mx[-1], b) for _, b in items[1:])
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            if j := bisect_right(prices, q):
                ans[i] = mx[j - 1]
        return ans
