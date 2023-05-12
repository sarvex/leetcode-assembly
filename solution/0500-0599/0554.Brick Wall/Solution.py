class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for row in wall:
            width = 0
            for brick in row[:-1]:
                width += brick
                cnt[width] += 1
        return len(wall) if not cnt else len(wall) - cnt[max(cnt, key=cnt.get)]
