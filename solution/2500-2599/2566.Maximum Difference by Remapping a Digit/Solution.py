class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mi = int(s.replace(s[0], '0'))
        return next((int(s.replace(c, '9')) - mi for c in s if c != '9'), num - mi)
