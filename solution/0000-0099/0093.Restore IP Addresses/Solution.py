class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            return False if not (0 <= int(s) <= 255) else s[0] != '0' or len(s) <= 1

        def dfs(s, t):
            if len(t) == 4:
                if not s:
                    ans.append('.'.join(t))
                return
            for i in range(1, min(4, len(s) + 1)):
                if check(s[:i]):
                    t.append(s[:i])
                    dfs(s[i:], t)
                    t.pop()

        ans = []
        dfs(s, [])
        return ans
