class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        ans = 0
        for i in range(1, 121):
            n1 = counter[i]
            for j in range(1, 121):
                if j > 0.5 * i + 7 and j <= i and (j <= 100 or i >= 100):
                    n2 = counter[j]
                    ans += n1 * n2
                    if i == j:
                        ans -= n2
        return ans
