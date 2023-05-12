class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for i, c in enumerate(command):
            if c == '(':
                ans.append('o' if command[i + 1] == ')' else 'al')
            elif c == 'G':
                ans.append(c)
        return ''.join(ans)
