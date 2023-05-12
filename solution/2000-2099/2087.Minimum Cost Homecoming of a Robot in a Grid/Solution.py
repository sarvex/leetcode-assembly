class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        i, j = startPos
        x, y = homePos
        ans = 0
        ans += sum(rowCosts[i + 1 : x + 1]) if i < x else sum(rowCosts[x:i])
        ans += sum(colCosts[j + 1 : y + 1]) if j < y else sum(colCosts[y:j])
        return ans
