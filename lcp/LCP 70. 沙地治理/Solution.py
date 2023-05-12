class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
        ans = [[1, 1]]
        k = 0
        for i in range(size, 1, -1):
            if k == 0:
                ans.extend([i, j] for j in range(1, i << 1, 2))
            elif k == 1:
                ans.append([i, 2])
            elif k == 2:
                ans.extend([i, j] for j in range(3, i << 1, 2))
            else:
                ans.append([i, 1])
            k = (k + 1) % 4
        return ans
