class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        s = sum(max(0, a - b) for a, b in transactions)
        ans = 0
        for a, b in transactions:
            ans = max(ans, s + b) if a > b else max(ans, s + a)
        return ans
