class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        ans.extend(ans[-1] ^ e for e in encoded)
        return ans
