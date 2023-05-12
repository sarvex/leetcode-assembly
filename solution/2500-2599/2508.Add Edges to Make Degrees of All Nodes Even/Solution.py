class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        vs = [i for i, v in g.items() if len(v) & 1]
        if not vs:
            return True
        if len(vs) == 2:
            a, b = vs
            if a not in g[b]:
                return True
            return any(a not in g[c] and c not in g[b] for c in range(1, n + 1))
        if len(vs) == 4:
            a, b, c, d = vs
            if a not in g[b] and c not in g[d]:
                return True
            return a not in g[d] and b not in g[c] if a in g[c] or b in g[d] else True
        return False
