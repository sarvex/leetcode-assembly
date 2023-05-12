class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        return sum(
            (total - (x * cost1)) // cost2 + 1 for x in range(total // cost1 + 1)
        )
