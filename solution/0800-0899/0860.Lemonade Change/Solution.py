class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for v in bills:
            if v == 10:
                ten += 1
                five -= 1
            elif v == 5:
                five += 1
            elif ten:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
