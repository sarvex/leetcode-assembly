class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        xors.extend(xors[-1] ^ v for v in arr)
        return [xors[l] ^ xors[r + 1] for l, r in queries]
