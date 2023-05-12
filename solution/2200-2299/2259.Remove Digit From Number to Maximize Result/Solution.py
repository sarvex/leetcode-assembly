class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = -1
        n = len(number)
        for i, d in enumerate(number):
            if d == digit:
                last = i
                if last + 1 < n and d < number[last + 1]:
                    break
        return number[:last] + number[last + 1 :]
